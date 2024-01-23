<script>
    console.log('test')
    import {auth, db} from "../firebase.js"; // Your Firebase initialization file // Import Firestore
    import {GoogleAuthProvider, signInWithPopup} from "firebase/auth";
    import {getDownloadURL, getStorage, ref, uploadBytesResumable} from "firebase/storage";
    import {onMount} from "svelte";
    import {navigate} from "svelte-routing";
    import {collection, doc, setDoc} from "firebase/firestore";
    import RegisterStart from "../components/RegisterStart.svelte";

    let user = null;
    let step = 0; // Start with step 1

    onMount(() => {
        auth.onAuthStateChanged(async (firebaseUser) => {
            if (firebaseUser) {
                // User is signed in.
                user = firebaseUser;
                await setDoc(doc(db, "users", user.uid), {
                    user_id: user.uid,
                    invited_by: new URLSearchParams(window.location.search).get(
                        "invite_code"
                    )
                }, {merge: true})
                step = 2; // Move to step 2 after successful login
            } else {
                // No user is signed in.
                step = 0;
            }
        });
    });

    async function signInWithGoogle() {
        const provider = new GoogleAuthProvider();
        auth.useDeviceLanguage();
        try {
            const result = await signInWithPopup(auth, provider);
        } catch (error) {
            console.error("Error signing in with Google", error);
            // Handle sign-in errors here
        }
    }

    function signOut() {
        auth.signOut();
        step = 0; // Return to step 1
        navigate("/"); // Navigate to the home page
    }

    let photoURL = '';
    let uploadError = '';
    let uploadProgress = 0;

    async function uploadPhoto(event) {
        const file = event.target.files[0];
        if (!file) {
            uploadError = 'no file uploaded';
        }
        // 1 mb limit
        if (file.size / (1000 * 1000) > 20) {
            uploadError = 'file is too big, max 20Mb';
        }
        const storage = getStorage();
        const fileRef = ref(storage, 'user_photos/' + user.uid + '/' + file.name);

        try {
            const uploadTask = uploadBytesResumable(fileRef, file);

            uploadTask.on('state_changed', (snapshot) => {
                // Observe state change events such as progress, pause, and resume
                uploadProgress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            }, (error) => {
                // Handle unsuccessful uploads
                console.error('Upload failed', error);
            }, () => {
                // Handle successful uploads on complete
                getDownloadURL(uploadTask.snapshot.ref).then(async (downloadURL) => {
                    photoURL = downloadURL;
                    await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                        photo: photoURL,
                    }, {merge: true});
                });
            });
        } catch (error) {
            console.error('Error uploading photo:', error);
        }
    }

    let jobTitle = "";
    let company = "";

    async function saveJobInfo() {
        if (!jobTitle) {
            console.log("Job title is required");
            return;
        }

        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                jobTitle,
                company,
            }, {merge: true});
            step++
            console.log('here')
        } catch (error) {
            console.error("Error saving job info:", error);
        }
    }

    const activities = ["Reading", "Writing", "Coding", "Hiking", "Cycling", "Cooking", "Photography"];
    let selectedActivities = new Set();

    function toggleActivity(activity) {
        if (selectedActivities.has(activity)) {
            selectedActivities.delete(activity);
        } else {
            selectedActivities.add(activity);
        }
        selectedActivities = selectedActivities
    }

    async function saveActivities() {
        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                hobbies: Array.from(selectedActivities)
            }, {merge: true});

            step++
        } catch (error) {
            console.error("Error saving activities:", error);
        }
    }

    const traits = ["Enthusiastic", "Positive", "Chill", "Anxious"];
    let selectedTraits = new Set();

    function toggleTrait(trait) {
        if (selectedTraits.has(trait)) {
            selectedTraits.delete(trait);
        } else {
            selectedTraits.add(trait);
        }
        selectedTraits = selectedTraits
    }

    async function saveTraits() {
        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                traits: Array.from(selectedTraits)
            }, {merge: true});

            step++
        } catch (error) {
            console.error("Error saving activities:", error);
        }
    }

    let selectedLanguages = [];
    let languageOptions = ['English', 'German', 'Other'];

    function addLanguage() {
        selectedLanguages = [...selectedLanguages, ''];
    }

    function updateLanguage(index, event) {
        selectedLanguages[index] = event.target.value;
    }

    function removeLanguage(index) {
        selectedLanguages.splice(index, 1);
        selectedLanguages = [...selectedLanguages];
    }

    async function saveLanguages() {
        const userLanguages = selectedLanguages;

        if (userLanguages.length === 0) {
            console.log("Please select at least one language.");
            return;
        }

        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                languages: userLanguages
            }, {merge: true});
            step++
        } catch (error) {
            console.error("Error saving languages:", error);
        }
    }

    let socials = "";

    async function saveSocials() {
        if (!socials) {
            console.log("social  is required");
            return;
        }

        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                socials,
            }, {merge: true});
            step++
        } catch (error) {
            console.error("Error saving socials info:", error);
        }
    }

    const promptQuestions = [
        "What’s something you’re passionate about and why?",
        "What’s a recent challenge you’ve overcome, and how did you do it?",
        "Describe an experience that significantly shaped who you are today.",
        "What are you looking for in a friendship and what are your expectations from a friend?",
        "What’s a cause or issue you feel strongly about?",
        "Can you describe a perfect day for you?",
        "What are the main things that shaped you the way you are right now?",
        "What's the most important thing in your life?",
        "Who are the public persons you truly admire, why?"
    ];

    let selectedPrompts = [{question: '', answer: ''}, {question: '', answer: ''}];

    let inviteCode = ''

    async function savePromptAnswers() {
        try {
            inviteCode = auth.currentUser.uid.slice(auth.currentUser.uid.length - 6)
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                prompts: selectedPrompts,
                onboarding_finished: true,
                invite_code: inviteCode
            }, {merge: true});

            step++
        } catch (error) {
            console.error("Error saving prompt answers:", error);
        }
    }

    function copyInviteLink() {
        const host = window.location.hostname;
        const inviteLink = `${host}?invite_code=${inviteCode}`;
        navigator.clipboard.writeText(inviteLink)
            .then(() => alert('Invite link copied to clipboard!'))
            .catch(err => console.error('Error copying invite link:', err));
    }
    console.log(step)
</script>
{#if step === 0}
    <div>aaa</div>
    <div>aaa</div>
    <div>aaa</div>
    <RegisterStart/>
{:else if step === 1}
<!--    <div class="step-container">-->
<!--        <button on:click={signInWithGoogle} class="google-auth-button">-->
<!--            Sign in with Google-->
<!--        </button>-->
<!--    </div>-->
{:else if step === 2}
    <div class="step-container">
        <form on:submit|preventDefault>
            <label for="photo-upload" class="custom-file-upload">
                Upload your photo
            </label>
            <input type="file" id="photo-upload" on:change={uploadPhoto}/>
            {#if uploadError}
                <p>{uploadError}</p>
            {:else if uploadProgress > 0 && uploadProgress < 100}
                <progress value={uploadProgress} max="100">Uploading...</progress>
            {:else if uploadProgress === 100}
                <p>Upload complete!</p>
                <button on:click={()=> step=3}>Next</button>
            {/if}
        </form>
    </div>
{:else if step === 3}
    <div class="step-container">
        <div>
            <input type="text" bind:value={jobTitle} placeholder="Job Title" required>
            <input type="text" bind:value={company} placeholder="Company (Optional)">
            <button on:click={() => step--}>Back</button>
            {#if jobTitle}
                <button on:click={saveJobInfo}>Next</button>
            {/if}
        </div>
    </div>
{:else if step === 4}
    <div class="step-container">
        <div class="activities-container">
            {#each activities as activity}
                <button
                        class="activity-button {selectedActivities.has(activity) ? 'selected' : ''}"
                        on:click={() => toggleActivity(activity)}>
                    {activity}
                </button>
            {/each}
            <button on:click={() => step--}>Back</button>
            {#if selectedActivities.size > 2}
                <button on:click={saveActivities}>Continue</button>
            {:else}
                <p>Select at least 3 hobbies</p>
            {/if}
        </div>
    </div>
{:else if step === 5}
    <div class="step-container">
        <div class="activities-container">
            {#each traits as trait}
                <button
                        class="activity-button {selectedTraits.has(trait) ? 'selected' : ''}"
                        on:click={() => toggleTrait(trait)}>
                    {trait}
                </button>
            {/each}
            <button on:click={() => step--}>Back</button>
            {#if selectedTraits.size > 1}
                <button on:click={saveTraits}>Continue</button>
            {:else}
                <p>Select at least 2 traits</p>
            {/if}
        </div>
    </div>
{:else if step === 6}
    <div>
        {#each selectedLanguages as language, index (index)}
            <div class="language-selection">
                <select bind:value={language} on:change={(event) => updateLanguage(index, event)}>
                    <option value="" disabled>Select a language</option>
                    {#each languageOptions as option}
                        <option value={option}>{option}</option>
                    {/each}
                </select>
                {#if index > 0}
                    <button on:click={() => removeLanguage(index)}>Remove</button>
                {/if}
            </div>
        {/each}
        <button on:click={addLanguage}>Add Another</button>
        <button on:click={() => step--}>Back</button>
        {#if selectedLanguages.filter(x => x).length > 0}
            <button on:click={saveLanguages}>Continue</button>
        {:else}
            <p>Select at least 1 language</p>
        {/if}
    </div>
{:else if step === 7}
    <div class="step-container">
        <div>
            <input type="text" bind:value={socials} placeholder="Social media" required>
            <button on:click={() => step--}>Back</button>
            {#if socials}
                <button on:click={saveSocials}>Next</button>
            {/if}
        </div>
    </div>
{:else if step === 8}
    <div class="step-container">
        <div>
            {#each selectedPrompts as prompt, index (index)}
                <div class="prompt-selection">
                    <select bind:value={prompt.question}>
                        <option value="" disabled>Select a question</option>
                        {#each promptQuestions as question}
                            <option value={question}>{question}</option>
                        {/each}
                    </select>
                    <textarea bind:value={prompt.answer} placeholder="Your answer"></textarea>
                </div>
            {/each}
            <button on:click={savePromptAnswers}>Continue</button>
        </div>
    </div>
{:else if step === 9}
    <div class="step-container">
        <div>
            <p>Congrats, you are on the waiting list! We will select 20 users who have invited most friends in other
                cities to join the app. Here is your invite code:</p>
            <p>{inviteCode}</p>
            <button on:click={copyInviteLink}>Share</button>
        </div>
    </div>
{/if}
<style>
    .activities-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        padding: 20px;
    }

    .activity-button {
        background-color: #f0f0f0;
        border: 2px solid black;
        border-radius: 20px;
        padding: 8px 16px;
        font-size: 16px;
        color: black;
        cursor: pointer;
        transition: background-color 0.3s, border-color 0.3s;
    }

    .activity-button:hover {
        background-color: #e0e0e0;
    }

    .activity-button.selected {
        background-color: #4CAF50;
        color: white;
        border-color: #4CAF50;
    }

    button {
        background-color: #008CBA;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin: 0 10px;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #007B9E;
    }
</style>
