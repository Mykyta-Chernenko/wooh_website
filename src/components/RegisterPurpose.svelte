<script>
    import {onMount} from 'svelte';
    import {collection, doc, getDoc, setDoc} from 'firebase/firestore';
    import {auth, db} from '../firebase.js';
    import {nextStep} from "../stores/stepStore.js";

    let loading = false;
    let selectedPurposes = new Set();
    const purposes = [
        "🍻 Grab a Beer",
        "📷 Do Hobbies",
        "🚶‍ Have Walks",
        "💃 Party",
        "✈️ Travel",
        "🚴️ Train",
        "📅 Visit Events",
        "🐕 Walk Pets",
        "💼 Discuss Job",
        "⛩️ Share Religion",
        "🌎 Exchange Cultures",
        "📚 Study",
        "🔡 Exchange Languages",
        "🌭 Eat",
        "👭 Be Couple Friends",
        "👪 Be Friends With Kids",
        "🤔 Other",
    ];

    const togglePurpose = (purpose) => {
        if (selectedPurposes.has(purpose)) {
            selectedPurposes.delete(purpose);
        } else if (selectedPurposes.size < 5) {
            selectedPurposes.add(purpose);
        }
        selectedPurposes = new Set(selectedPurposes);
    };


    onMount(async () => {
        loading = true;
        try {
            const docRef = doc(collection(db, 'users'), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                selectedPurposes = new Set(docSnap.data().purposes || []);
            }
        } catch (error) {
            console.error('Error fetching user data:', error);
        }
        loading = false;
    });

    const next = async () => {
        try {
            await setDoc(doc(collection(db, 'users'), auth.currentUser.uid), {
                purposes: Array.from(selectedPurposes)
            }, {merge: true});
            nextStep()
        } catch (error) {
            console.error('Error saving selection:', error);
        }
    };
    $: buttonEnabled = selectedPurposes.size > 0

</script>


<div class="content-box">
    <div class="center">
        <div class="question-container">
            <div class="onboarding-h1">What do you want to do with a new friend?</div>
        </div>
        <div class="question-container purpose">
            <div class="question">Choose 1-5 things:</div>
            <div class="option-box">
                {#each purposes as purpose}
                    <div on:click={() => togglePurpose(purpose)} on:keypress={() => togglePurpose(purpose)}
                         class="option {selectedPurposes.has(purpose) ? 'selected' : ''}">
                        <div class="option-text">{purpose}</div>
                    </div>
                {/each}
            </div>
        </div>


    </div>

    <button class="btn next-button" on:click={next} disabled={!buttonEnabled || loading}>next</button>
</div>

<style>
    .purpose {
        margin-top: 20px;
    }
</style>
