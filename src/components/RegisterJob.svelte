<script>
    import {onMount} from "svelte";
    import {nextStep} from "../stores/stepStore.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";
    import {tracking} from "../tracking.js";

    let loading = false
    let job = ""
    const handleInput = (event) => {
        job = event.target.value;
    };


    onMount(async () => {
        tracking.track("OnboardingJobLoaded");
        loading = true
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                job = docSnap.data().job || "";
            }
        } catch (error) {
            tracking.track("OnboardingJobError", {error: JSON.stringify(error)});
        }
        loading = false;
    });

    $: buttonEnabled = !!job;
    const next = async () => {
        tracking.track("OnboardingJobNext", {job});
        loading = true
        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                job,
            }, {merge: true});
            nextStep()
        } catch (error) {
            tracking.track("OnboardingJobError", {error: JSON.stringify(error)});
        }
        loading = false
    }
</script>

<style>

</style>

<div class="content-box">
    <form on:submit|preventDefault={next}>
        <div class="center">
            <div class="onboarding-h1">What do you do for living?</div>
            <div class="input-container" style="margin-top: 20px">
                <div class="question">Enter your job title</div>
                <div class="input-box">
                    <div class="input-icon">🎒</div>
                    <input type="text" placeholder="eg. Designer" bind:value={job} on:input={handleInput}
                           class="input" autofocus/>
                </div>
            </div>
        </div>
        <button class="btn next-button" disabled={!buttonEnabled || loading}>next</button>
    </form>
</div>
