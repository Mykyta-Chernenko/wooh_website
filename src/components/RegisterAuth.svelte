<script>
    import {GoogleAuthProvider, OAuthProvider, signInWithPopup} from "firebase/auth";
    import {auth, db} from "../firebase.js";
    import {collection, doc, getDoc, setDoc} from "firebase/firestore";
    import {tracking} from "../tracking.js";
    import {onMount} from "svelte";
    import {nextStep, step, TOTAL_STEPS} from "../stores/stepStore.js";

    onMount(()=>{
        tracking.track("OnboardingAuthLoaded");
        const loadUser = async () => {
            if (auth.currentUser) {
                const docRef = doc(collection(db, "users"), auth.currentUser.uid);
                const docSnap = await getDoc(docRef);
                if (docSnap.exists() && docSnap.data().onboarding_finished) {
                    tracking.track("OnboardingAuthRedirectingToWaitlist");
                    step.set(TOTAL_STEPS)
                }
                else {
                    nextStep()
                }
            }
        }
        void loadUser()
    })
    async function commonAuth() {
        const user = auth.currentUser;
        tracking.identify(user.uid);
        tracking.alias(user.uid);
        tracking.track("OnboardingAuthFinished");
        const docRef = doc(collection(db, 'users'), user.uid);
        const docSnap = await getDoc(docRef);

        if (docSnap.exists()) {
          await setDoc(doc(db, "users", user.uid), {
            user_id: user.uid,
            email: user.email,
            signed_in_at: new Date().toISOString()
          }, {merge: true})
        } else{
          await setDoc(doc(db, "users", user.uid), {
            user_id: user.uid,
            email: user.email,
            created_at: new Date().toISOString(),
          }, {merge: true})
        }
        const inviteCode = new URLSearchParams(window.location.search).get(
            "invite_code"
        )
        if (inviteCode) {
            await setDoc(doc(db, "users", user.uid), {
                invited_by: inviteCode,
            }, {merge: true})
        }
        nextStep()
    }

    async function signInWithGoogle() {
        tracking.track("OnboardingAuthGoogleInitiated");
        const provider = new GoogleAuthProvider();
        provider.addScope("email")
        auth.useDeviceLanguage();
        try {
            const result = await signInWithPopup(auth, provider);
            tracking.track("OnboardingAuthGoogleResult", {result: JSON.stringify(result)});
            await commonAuth()
        } catch (error) {
            tracking.track("OnboardingAuthGoogleError", {error: JSON.stringify(error)});
        }
    }

    async function signInWithApple() {
        tracking.track("OnboardingAuthAppleInitiated");
        const provider = new OAuthProvider('apple.com');
        provider.addScope('email');
        auth.useDeviceLanguage();
        try {
            const result = await signInWithPopup(auth, provider);
            tracking.track("OnboardingAuthAppleResult", {result: JSON.stringify(result)});
            await commonAuth()
        } catch (error) {
            tracking.track("OnboardingAuthAppleError", {error: JSON.stringify(error)});
        }
    }
</script>

<style>


    .apple-button {
        width: 100%;
        margin-top: 10px;
        padding: 16px 0;
        background: black;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.17);
        border-radius: 8px;
        justify-content: center;
        align-items: center;
        gap: 4px;
        display: inline-flex;
        color: white;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        cursor: pointer;
    }

    .google-button {
        width: 100%;
        margin-top: 20px;
        padding: 16px 0;
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        justify-content: center;
        align-items: center;
        gap: 4px;
        display: inline-flex;
        color: black;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        cursor: pointer;
    }

    .terms {
        margin-top: 30px;
        width: 100%;
        text-align: center;
        color: rgba(0, 0, 0, 0.70);
        font-weight: 500;
        font-size: 12px;
        line-height: 16px;
        letter-spacing: 0.24px;
        word-wrap: break-word;
    }

    .underline {
        font-weight: 500;
        text-decoration: underline;
        cursor: pointer
    }

</style>

<div class="content-box">
    <div></div>
    <div class="center">
        <div class="onboarding-h1">Create account</div>
        <div class="google-button" on:click={signInWithGoogle} on:keypress={signInWithGoogle}>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                <rect width="20" height="20" fill="white"/>
                <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M19.599 10.2271C19.599 9.518 19.5354 8.83619 19.4172 8.18164H9.99902V12.0498H15.3808C15.149 13.2998 14.4445 14.3589 13.3854 15.068V17.5771H16.6172C18.5081 15.8362 19.599 13.2725 19.599 10.2271Z"
                      fill="#4285F4"/>
                <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M9.99886 19.9999C12.6989 19.9999 14.9625 19.1044 16.617 17.5772L13.3852 15.0681C12.4898 15.6681 11.3443 16.0226 9.99886 16.0226C7.39432 16.0226 5.18977 14.2635 4.40341 11.8999H1.0625V14.4908C2.70795 17.759 6.08977 19.9999 9.99886 19.9999Z"
                      fill="#34A853"/>
                <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M4.40455 11.9002C4.20455 11.3002 4.09091 10.6593 4.09091 10.0002C4.09091 9.3411 4.20455 8.70019 4.40455 8.10019V5.50928H1.06364C0.386364 6.85928 0 8.38655 0 10.0002C0 11.6138 0.386364 13.1411 1.06364 14.4911L4.40455 11.9002Z"
                      fill="#FBBC05"/>
                <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M9.99886 3.97727C11.467 3.97727 12.7852 4.48182 13.8216 5.47273L16.6898 2.60455C14.958 0.990909 12.6943 0 9.99886 0C6.08977 0 2.70795 2.24091 1.0625 5.50909L4.40341 8.1C5.18977 5.73636 7.39432 3.97727 9.99886 3.97727Z"
                      fill="#EA4335"/>
            </svg>
            Continue with Google
        </div>
        <div class="apple-button" on:click={signInWithApple} on:keypress={signInWithApple}>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                <rect width="20" height="20" fill="black"/>
                <path d="M17.7338 15.3531C17.444 16.0228 17.1009 16.6392 16.7034 17.2059C16.1615 17.9784 15.7178 18.5132 15.3759 18.8101C14.8459 19.2976 14.278 19.5472 13.6699 19.5614C13.2334 19.5614 12.7069 19.4372 12.094 19.1852C11.4792 18.9344 10.9141 18.8101 10.3975 18.8101C9.85563 18.8101 9.2745 18.9344 8.6529 19.1852C8.03036 19.4372 7.52884 19.5685 7.1454 19.5815C6.56226 19.6064 5.98101 19.3496 5.40082 18.8101C5.03051 18.4872 4.56733 17.9335 4.01246 17.1491C3.41713 16.3115 2.92768 15.3401 2.54424 14.2328C2.13359 13.0367 1.92773 11.8784 1.92773 10.7571C1.92773 9.47259 2.20529 8.36475 2.76122 7.43638C3.19814 6.69067 3.77939 6.10244 4.50687 5.67061C5.23436 5.23878 6.0204 5.01873 6.86691 5.00465C7.33009 5.00465 7.93749 5.14792 8.6923 5.4295C9.44498 5.71202 9.92827 5.85529 10.1402 5.85529C10.2986 5.85529 10.8355 5.68777 11.7456 5.35378C12.6063 5.04405 13.3327 4.9158 13.9278 4.96632C15.5404 5.09646 16.7519 5.73213 17.5576 6.87737C16.1154 7.7512 15.402 8.9751 15.4162 10.5452C15.4292 11.7681 15.8728 12.7858 16.7448 13.5939C17.1399 13.9689 17.5812 14.2588 18.0722 14.4646C17.9657 14.7734 17.8533 15.0692 17.7338 15.3531ZM14.0355 0.799946C14.0355 1.7585 13.6853 2.65349 12.9873 3.48189C12.1449 4.4667 11.126 5.03577 10.0211 4.94597C10.0071 4.83097 9.9989 4.70994 9.9989 4.58276C9.9989 3.66255 10.3995 2.67775 11.1109 1.87254C11.4661 1.46484 11.9178 1.12585 12.4655 0.855433C13.0121 0.589048 13.5291 0.441731 14.0154 0.416504C14.0296 0.544647 14.0355 0.672799 14.0355 0.799934V0.799946Z"
                      fill="white"/>
            </svg>
            Continue with Apple
        </div>
        <div class="terms">
            <span>By clicking Continue you agree to our </span>
            <span class="underline">Terms of Service </span>
            <span>and have read and understand the </span>
            <span class="underline">Privacy Policy</span>
        </div>
    </div>

    <div>
    </div>
</div>
