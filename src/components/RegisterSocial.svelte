<script>
    import {onMount} from "svelte";
    import {nextStep} from "../stores/stepStore.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";
    import {tracking} from "../tracking.js";

    let loading = false
    let instagram = ""
    let facebook = ""
    let linkedin = ""
    let otherSocial = ""


    onMount(async () => {
        tracking.track("OnboardingSocialLoaded");
        loading = true
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);

            if (docSnap.exists()) {
                instagram = docSnap.data().instagram || "";
                facebook = docSnap.data().facebook || "";
                linkedin = docSnap.data().linkedin || "";
                otherSocial = docSnap.data().otherSocial || "";
            }
        } catch (error) {
            tracking.track("OnboardingSocialError", {error: JSON.stringify(error)});
        }
        loading = false;
    });

    $: buttonEnabled = !!instagram || !!facebook || !!linkedin || otherSocial;
    const next = async () => {
        loading = true
        try {
            const inviteCode = auth.currentUser.uid.slice(auth.currentUser.uid.length - 6)
            tracking.track("OnboardingSocialNext", {
                instagram,
                facebook,
                linkedin,
                otherSocial,
                inviteCode
            });
            await setDoc(doc(collection(db, "users"), auth.currentUser.uid), {
                instagram,
                facebook,
                linkedin,
                otherSocial,
                inviteCode,
                onboarding_finished: true,
            }, {merge: true});
            nextStep()
        } catch (error) {
            tracking.track("OnboardingSocialError", {error: JSON.stringify(error)});
        }
        loading = false
    }
</script>

<style>
    .info-box {
        background: #E8E8E8;
        border-radius: 12px;
        border: 1px solid #DDD;
        padding: 14px 16px;
        font-size: 13px;
        font-weight: 500;
        color: black;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-top: 15px;
        line-height: 16px;
        letter-spacing: 0.26px;
    }

    .info-box > div {
        text-align: left;
    }

    .icon {
        height: 32px;
        width: 32px;
    }
</style>

<div class="content-box">
    <form on:submit|preventDefault={next}>

        <div class="center">
            <div class="onboarding-h1">Share link to one of your Social Media</div>
            <div class="info-box">
                <div class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                        <path d="M6.66797 17.3337C6.66797 16.6264 6.94892 15.9481 7.44902 15.448C7.94911 14.9479 8.62739 14.667 9.33464 14.667H22.668C23.3752 14.667 24.0535 14.9479 24.5536 15.448C25.0537 15.9481 25.3346 16.6264 25.3346 17.3337V25.3337C25.3346 26.0409 25.0537 26.7192 24.5536 27.2193C24.0535 27.7194 23.3752 28.0003 22.668 28.0003H9.33464C8.62739 28.0003 7.94911 27.7194 7.44902 27.2193C6.94892 26.7192 6.66797 26.0409 6.66797 25.3337V17.3337Z"
                              stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13 21C13 21.7956 13.3161 22.5587 13.8787 23.1213C14.4413 23.6839 15.2044 24 16 24C16.7956 24 17.5587 23.6839 18.1213 23.1213C18.6839 22.5587 19 21.7956 19 21C19 20.2044 18.6839 19.4413 18.1213 18.8787C17.5587 18.3161 16.7956 18 16 18C15.2044 18 14.4413 18.3161 13.8787 18.8787C13.3161 19.4413 13 20.2044 13 21Z"
                              fill="black"/>
                        <path d="M10.668 14.6667V9.33333C10.668 7.91885 11.2299 6.56229 12.2301 5.5621C13.2303 4.5619 14.5868 4 16.0013 4C17.4158 4 18.7723 4.5619 19.7725 5.5621C20.7727 6.56229 21.3346 7.91885 21.3346 9.33333V14.6667"
                              stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div>We use it only for verification. We will not share the link with anyone.</div>
            </div>
            <div class="input-container">
                <div class="question">Instagram</div>
                <div class="input-box">
                    <input type="text" placeholder="instagram.com/username" bind:value={instagram}
                           class="input" autofocus/>
                </div>
            </div>
            <div class="input-container">
                <div class="question">Facebook</div>
                <div class="input-box">
                    <input type="text" placeholder="facebook.com/username" bind:value={facebook}
                           class="input"/>
                </div>
            </div>
            <div class="input-container">
                <div class="question">Linkedin</div>
                <div class="input-box">
                    <input type="text" placeholder="linkedin.com/username" bind:value={linkedin}
                           class="input"/>
                </div>
            </div>
            <div class="input-container">
                <div class="question">Other</div>
                <div class="input-box">
                    <input type="text" placeholder="anywebsite.com" bind:value={otherSocial}
                           class="input"/>
                </div>
            </div>
        </div>

        <button class="btn next-button" disabled={!buttonEnabled || loading}>next</button>
    </form>
</div>
