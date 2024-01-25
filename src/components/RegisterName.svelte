<script>
    import {onMount} from "svelte";
    import {nextStep} from "../stores/stepStore.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";

    let loading = false
    let name = ""
    const handleInput = (event) => {
        name = event.target.value;
    };


    let selectedGender = undefined
    const selectGender = (gender) => {
        selectedGender = gender;
    };

    onMount(async () => {
        loading = true
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                name = docSnap.data().name || "";
                selectedGender = docSnap.data().selectedGender || undefined;
            }
        } catch (error) {
            console.error("Error fetching user data:", error);
        }
        loading = false;
    });

    $: buttonEnabled = !!name && !!selectedGender;
    const next = async () => {
        loading = true
        try {
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                name,
                selectedGender,
            }, {merge: true});
            nextStep()
        } catch (error) {
            console.error("Error saving name:", error);
        }
        loading = false
    }
</script>

<style>

</style>

<div class="content-box">
    <div class="center">
        <div class="input-container">
            <div class="question">How should we call you?</div>
            <div class="input-box">
                <div class="input-icon">👋</div>
                <input type="text" placeholder="Your first name" bind:value={name} on:input={handleInput}
                       class="input"/>
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

    <button class="btn next-button" on:click={next} disabled={!buttonEnabled || loading}>next</button>
</div>
