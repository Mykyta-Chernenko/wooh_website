<script>
    import {onMount} from "svelte";
    import {collection, doc, getDoc} from "firebase/firestore";
    import {auth, db} from "../firebase.js";
    import {tracking} from "../tracking.js";
    import InstallButton from './InstallPWA.svelte';
    let inviteLink = ""

    let notificationData = ""
    onMount(async () => {
        tracking.track("OnboardingWaitlistLoaded");
        try {
            const docRef = doc(collection(db, "users"), auth.currentUser.uid);
            const docSnap = await getDoc(docRef);
            const host = window.location.hostname;
            const code = docSnap.data().invite_code || auth.currentUser.uid.slice(auth.currentUser.uid.length - 6);
            inviteLink = `${host}/${code}`;
        } catch (error) {
            tracking.track("OnboardingWaitlistError", {error: JSON.stringify(error)});
        }
    });
    function askNotificationPermission() {
      Notification.requestPermission().then(async permission => {
        if(permission === "granted") {
          console.log("Notification permission granted.");
          function urlBase64ToUint8Array(base64String) {
            var padding = '='.repeat((4 - base64String.length % 4) % 4);
            var base64 = (base64String + padding)
              .replace(/\-/g, '+')
              .replace(/_/g, '/');

            var rawData = window.atob(base64);
            var outputArray = new Uint8Array(rawData.length);

            for (var i = 0; i < rawData.length; ++i) {
              outputArray[i] = rawData.charCodeAt(i);
            }
            return outputArray;
          }

// Your VAPID public key as a base64-encoded string (without PEM headers/footers and line breaks)
          const vapidPublicKey = 'BNlq3d77oPhV8YqxZwQTK3tJWeknnGnZP4bo6Oq-1XEmFJ_qsuDQ4TIjbBo_H_hou0xnC3J4iSvS6EtX3JWr-2U'
          const registration = await navigator.serviceWorker.ready;
          const pushSubscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(vapidPublicKey)
          });

          // Send the pushSubscription object to the server
          // You can use fetch() or another method to send the object
          notificationData=JSON.stringify(pushSubscription)
        } else {
          console.log("Notification permission denied.");
        }
      });
    }


    function copyInviteLink() {
        tracking.track("OnboardingWaitlistLinkCopied", {inviteLink});
        navigator.clipboard.writeText(inviteLink)
            .then(() => alert('Your invite link copied to clipboard!'))
            .catch(err => console.error('Error copying invite link:', err));
    }
</script>

<style>

    .info-box {
        max-width: 100%;
        text-align: center;
        background: #C4E5FF;
        border-radius: 12px;
        border: 1px solid #99CFF9;
        padding: 20px 16px;
        margin-bottom: 0;
        font-size: 13px;
        font-weight: 500;
        color: black;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        line-height: 16px;
        letter-spacing: 0.26px;
    }

    .content-box-block {
        max-width: 100%;
        margin-top: 20px;
        padding: 24px 20px;
        background: white;
        border-radius: 16px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        gap: 20px;
    }

    .absolute-text {
        color: black;
        font-size: 32px;
        font-weight: 500;
        line-height: 36px;
        word-wrap: break-word;
    }

    .share-button {
        display: inline-block;
        padding: 0 4px;
        border-radius: 8px;
        border: 1px solid #A693F3;
        align-items: center;
        justify-content: center;
        background: #CCC4FF;
        transform: rotate(-1deg);
    }


    .input-text {
        color: black;
        font-size: 16px;
        font-weight: 500;
        line-height: 20px;
        word-wrap: break-word;
    }

    .invite-block {
        width: 100%;
    }

    .copy-button {
        background: black;
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 4px;
        padding: 4px 8px;
    }

    .copy-button:hover {
        cursor: pointer;
    }

    .invite-top {
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 45px;
        background: white;
        border: 1px solid #DDD;
    }

    .instruction-container {
        align-self: stretch;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        gap: 12px;
    }

    .instruction-line {
        align-self: stretch;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 4px;
    }

    .instruction-text {
        flex: 1;
        color: black;
        font-size: 13px;
        font-weight: 500;
        line-height: 16px;
        letter-spacing: 0.26px;
        word-wrap: break-word;
        text-align: left;
    }

    .icon {
        color: white;
        background-color: black;
        height: 24px;
        width: 24px;
        font-size: 14px;
        font-weight: 500;
        line-height: 24px;
        border-radius: 99px;


    }

    .waitlist-title {
        font-size: 32px;
        line-height: 36px;
        letter-spacing: 0;
    }
</style>

<div class="content-box">
    <div class="center">
        <div style="width: 100%">
            <div class="info-box">
                Last step!
            </div>
        </div>

        <div class="content-box-block">
            <div>
                <div class="onboarding-h1 waitlist-title">To get inside our WOOH community
                    <span class="share-button">
                        share
                    </span>
                    your
                    invite link with 2+ friends.
                </div>

            </div>
            <div class="invite-block">
                <div class="invite-top">
                    <div class="input-text">{inviteLink}</div>
                </div>
                <div class="copy-button" on:click={copyInviteLink} on:keypress={copyInviteLink}>
                    <div style="color: white;">copy link</div>
                    <div style="height: 24px; width: 24px">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M5.01033 5.60756C4.59353 5.99657 4.35938 6.52419 4.35938 7.07433V13.8146C4.35938 14.087 4.41686 14.3567 4.52855 14.6084C4.64024 14.86 4.80395 15.0887 5.01033 15.2813C5.21671 15.474 5.46171 15.6267 5.73136 15.731C6.00101 15.8352 6.29001 15.8889 6.58187 15.8889H6.85938V9.704C6.85938 9.07526 7.12698 8.47227 7.60332 8.02769C8.07967 7.5831 8.72573 7.33333 9.39937 7.33333H16.026V7.07433C16.026 6.80193 15.9686 6.53219 15.8569 6.28052C15.7452 6.02885 15.5815 5.80018 15.3751 5.60756C15.1687 5.41494 14.9237 5.26214 14.6541 5.1579C14.3844 5.05365 14.0954 5 13.8035 5H6.58187C5.99243 5 5.42713 5.21855 5.01033 5.60756Z"
                                  fill="white"/>
                            <path d="M7.69271 10.1854C7.69271 9.6353 7.92686 9.10768 8.34366 8.71867C8.76046 8.32966 9.32576 8.11111 9.91521 8.11111H17.1369C17.4287 8.11111 17.7177 8.16477 17.9874 8.26901C18.257 8.37326 18.502 8.52605 18.7084 8.71867C18.9148 8.91129 19.0785 9.13996 19.1902 9.39163C19.3019 9.6433 19.3594 9.91304 19.3594 10.1854V16.9257C19.3594 17.1981 19.3019 17.4678 19.1902 17.7195C19.0785 17.9711 18.9148 18.1998 18.7084 18.3924C18.502 18.5851 18.257 18.7379 17.9874 18.8421C17.7177 18.9463 17.4287 19 17.1369 19H9.91521C9.62335 19 9.33434 18.9463 9.06469 18.8421C8.79505 18.7379 8.55004 18.5851 8.34366 18.3924C8.13728 18.1998 7.97358 17.9711 7.86189 17.7195C7.7502 17.4678 7.69271 17.1981 7.69271 16.9257V10.1854Z"
                                  fill="white"/>
                        </svg>
                    </div>
                </div>
            </div>
            <div class="instruction-container">
                <div class="instruction-line">
                    <div class="icon">1</div>
                    <div class="instruction-text" style="margin-left: 3px">Share the link with your friends.</div>
                </div>
                <div class="instruction-line">
                    <div class="icon">2</div>
                    <div class="instruction-text" style="margin-left: 3px">Wait for your friends to Sign Up.</div>
                </div>
                <div class="instruction-line">
                    <div class="icon">3</div>
                    <div class="instruction-text" style="margin-left: 3px">Receive an email to join the WOOH
                        App.
                    </div>
                </div>
            </div>
        </div>

        <div class="content-box-block" style="gap: 16px">

            <div class="absolute-text" on:click={askNotificationPermission}>💁‍♀️</div>
            <div class="absolute-text" style="font-size: 29px">Wait, but why invite?</div>
            <div style="text-align: left">
                <span class="instruction-text" style="color: black;">We want to maintain an active and engaged community. </span>
                <span class="instruction-text" style="color: rgba(0, 0, 0, 0.50);">Sharing the link with friends shows that you are ready for active participation.</span>
            </div>
        </div>
    </div>
    {#if notificationData}
        <InstallButton></InstallButton>
    {/if}
    <div style="margin: 40px; word-break: break-word">
    {notificationData}
    </div>
</div>
