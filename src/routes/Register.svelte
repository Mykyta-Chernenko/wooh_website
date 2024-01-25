<script>
    import RegisterHeader from "../components/RegisterHeader.svelte";
    import {auth} from "../firebase.js"; // Your Firebase initialization file // Import Firestore
    import {onMount} from "svelte";
    import RegisterStart from "../components/RegisterStart.svelte";
    import RegistrationProgress from "../components/RegistrationProgress.svelte";
    import {step} from "../stores/stepStore.js";
    import RegisterAuth from "../components/RegisterAuth.svelte";
    import RegisterName from "../components/RegisterName.svelte";
    import RegisterCity from "../components/RegisterCity.svelte";
    import RegisterJob from "../components/RegisterJob.svelte";
    import RegisterHobbies from "../components/RegisterHobbies.svelte";
    import RegisterPurpose from "../components/RegisterPurpose.svelte";
    import RegisterSocial from "../components/RegisterSocial.svelte";
    import RegisterWaitlist from "../components/RegisterWaitlist.svelte";

    onMount(() => {
        auth.onAuthStateChanged(async (firebaseUser) => {
            if (firebaseUser) {
                step.set(8);
            } else {
                step.set(0)
            }
        });
    });

</script>
<div class="content">
    <RegisterHeader/>
    <div class="main-content">
        <RegistrationProgress/>
        {#if $step === 0}
            <RegisterStart/>
        {:else if $step === 1}
            <RegisterAuth/>
        {:else if $step === 2}
            <RegisterName/>
        {:else if $step === 3}
            <RegisterCity/>
        {:else if $step === 4}
            <RegisterJob/>
        {:else if $step === 5}
            <RegisterHobbies/>
        {:else if $step === 6}
            <RegisterPurpose/>
        {:else if $step === 7}
            <RegisterSocial/>
        {:else if $step === 8}
            <RegisterWaitlist/>
        {/if}
    </div>
</div>
<style>
    .content {
        font-size: 14px;
        width: 100%;
        padding: 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .main-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 335px;
    }
</style>
