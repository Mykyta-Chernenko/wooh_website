<script>
    import {onMount} from "svelte";
    import {nextStep} from "../stores/stepStore.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";

    let loading = false
    let job = ""
    const handleInput = (event) => {
        job = event.target.value;
    };


    onMount(async () => {
        loading = true
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                job = docSnap.data().job || "";
            }
        } catch (error) {
            console.error("Error fetching user data:", error);
        }
        loading = false;
    });

    $: buttonEnabled = !!job;
    const next = async () => {
        loading = true
        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                job,
            }, {merge: true});
            nextStep()
        } catch (error) {
            console.error("Error saving job:", error);
        }
        loading = false
    }
</script>

<style>

</style>

<div class="content-box">
    <div></div>
    <div class="center">
        <div class="onboarding-h1">What do you do for living?</div>
        <div class="input-container" style="margin-top: 20px">
            <div class="question">Enter your job title</div>
            <div class="input-box">
                <div class="input-icon">🎒</div>
                <input type="text" placeholder="eg. Designer" bind:value={job} on:input={handleInput}
                       class="input"/>
            </div>
        </div>
    </div>
    <div></div>

    <button class="btn next-button" on:click={next} disabled={!buttonEnabled || loading}>next</button>
</div>
