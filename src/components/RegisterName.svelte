<script>
    import {onMount} from "svelte";
    import {nextStep} from "../stores/stepStore.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";
    import {tracking} from "../tracking.js";

    let loading = false
    let name = ""
    const handleInput = (event) => {
        name = event.target.value;
    };


    let selectedGender = undefined
    const selectGender = (gender) => {
        selectedGender = gender;
    };

    const mountData = async () => {
        loading = true
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);
            if (docSnap.exists()) {
                name = docSnap.data().name || "";
                selectedGender = docSnap.data().selectedGender || undefined;
            }
        } catch (error) {
            tracking.track("OnboardingNameError", {error: JSON.stringify(error)});
        }
        loading = false;
    }
    onMount(async () => {
        tracking.track("OnboardingNameLoaded");
        await mountData()
        auth.onAuthStateChanged(async () => {
            await mountData()
        });
    });

    $: buttonEnabled = !!name && !!selectedGender;
    const next = async () => {
        loading = true
        try {
            tracking.track("OnboardingNameNext", {name, selectedGender});
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                name,
                selectedGender,
            }, {merge: true});
            nextStep()
        } catch (error) {
            tracking.track("OnboardingNameError", {error: JSON.stringify(error)});
        }
        loading = false
    }
</script>

<style>

</style>

<div class="content-box">
    <form on:submit|preventDefault={next}>

        <div class="center">
            <div class="input-container">
                <div class="question">How should we call you?</div>
                <div class="input-box">
                    <div class="input-icon">👋</div>
                    <input type="text" placeholder="Your first name" bind:value={name} on:input={handleInput}
                           class="input" autofocus/>
                </div>
            </div>
            <div class="option-container">
                <div class="question">What gender best describes you?</div>
                <div class="option-box">
                    {#each ['Woman', 'Man', 'Other', 'Prefer not to say'] as gender}
                        <div on:click={() => selectGender(gender)} on:keypress={() => selectedGender(gender)}
                             class="option {selectedGender === gender ? 'selected' : ''}">
                            <div class="option-text">{gender}</div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <button class="btn next-button" disabled={!buttonEnabled || loading}>next</button>
    </form>
</div>
