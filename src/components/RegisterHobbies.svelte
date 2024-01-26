<script>
    import {onMount} from 'svelte';
    import {collection, doc, getDoc, setDoc} from 'firebase/firestore';
    import {auth, db} from '../firebase.js';
    import {nextStep} from "../stores/stepStore.js";
    import {tracking} from "../tracking.js";

    let loading = false;
    let selectedHobbies = new Set();
    const hobbies = [
        "🍳 Cooking",
        "🎵 Music",
        "🎨 Arts",
        "👗 Fashion",
        "🧘 Health",
        "✈️ Travel",
        "🚴 Cycling",
        "🍷 Wine",
        "📚 Reading",
        "🎮 Gaming",
        "🎥 Films",
        "🏋️ Fitness",
        "🧗 Climbing",
        "🌿 Yoga",
        "🎲 BoardGames",
        "📷 Photography",
        "💃 Parties",
        "🐕 Pets",
        "🏞️ Nature",
        "🌱 Gardening",
        "📖 Writing",
        "💻 Tech",
        "🧘‍ Mental Health",
        "🥾 Hiking",
        "🧪 Science",
    ];

    const toggleHobby = (hobby) => {
        if (selectedHobbies.has(hobby)) {
            selectedHobbies.delete(hobby);
        } else if (selectedHobbies.size < 10) {
            selectedHobbies.add(hobby);
        }
        selectedHobbies = new Set(selectedHobbies);
    };


    onMount(async () => {
        tracking.track("OnboardingHobbiesLoaded");
        loading = true;
        try {
            const docRef = doc(collection(db, 'users'), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                selectedHobbies = new Set(docSnap.data().hobbies || []);
            }
        } catch (error) {
            tracking.track("OnboardingHobbiesError", {error: JSON.stringify(error)});
        }
        loading = false;
    });

    const next = async () => {
        tracking.track("OnboardingHobbiesNext", {hobbies});
        try {
            await setDoc(doc(collection(db, 'users'), auth.currentUser.uid), {
                hobbies: Array.from(selectedHobbies)
            }, {merge: true});
            nextStep()
        } catch (error) {
            tracking.track("OnboardingHobbiesError", {error: JSON.stringify(error)});
        }
    };
    $: buttonEnabled = selectedHobbies.size > 0

</script>


<div class="content-box">
    <form on:submit|preventDefault={next}>
        <div class="center">
            <div class="question-container">
                <div class="onboarding-h1">What are your greatest interests?</div>
            </div>
            <div class="question-container hobby">
                <div class="question">Choose 1-10 hobbies:</div>
                <div class="option-box">
                    {#each hobbies as hobby}
                        <div on:click={() => toggleHobby(hobby)} on:keypress={() => toggleHobby(hobby)}
                             class="option {selectedHobbies.has(hobby) ? 'selected' : ''}">
                            <div class="option-text">{hobby}</div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <button class="btn next-button" disabled={!buttonEnabled || loading}>next</button>
    </form>
</div>

<style>
    .hobby {
        margin-top: 20px;
    }
</style>
