<script>
    import {get} from 'svelte/store';

    import {signOut, step} from '../stores/stepStore';
    import {tracking} from "../tracking.js";

    async function goBack() {
        tracking.track("OnboardingGoBack", {currentStep: get(step)});
        if (get(step) === 0) {
            const inviteCode = new URLSearchParams(window.location.search).get(
                "invite_code"
            ) || ''
            window.location.href = '/' + inviteCode;
            return
        } else if (get(step) === 2) {
            await signOut()
        }
        step.update(step => step - 1);
    }


</script>
<style>
    .nav-bar {
        width: 100%;
        min-height: 90px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }


    .logo-icon {
        width: 128px;
        height: 42px;
    }

    .back-icon {
        width: 24px;
        height: 24px;
    }

    .back-icon:hover {
        cursor: pointer;
    }
</style>

<div class="nav-bar">
    <div class="back-icon" on:click={goBack} on:keypress={goBack}>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <g clip-path="url(#clip0_605_3280)">
                <path d="M10 5L3 12L10 19" stroke="black" stroke-width="3"/>
                <path d="M3 12H20.4852" stroke="black" stroke-width="3"/>
            </g>
            <defs>
                <clipPath id="clip0_605_3280">
                    <rect width="24" height="24" fill="white"/>
                </clipPath>
            </defs>
        </svg>
    </div>
    <div class="logo-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="128" height="42" viewBox="0 0 128 42" fill="none">
            <path d="M45.0859 34.6943C50.9575 37.6619 58.4683 39.0097 69.135 39.0097C79.8017 39.0097 87.3125 37.6619 93.1841 34.6943"
                  stroke="black" stroke-width="5"/>
            <path d="M3.61154 28.0289L0 0.549805H5.14252L7.81192 24.4174H8.51853L11.973 0.549805H20.9234L24.3779 24.4174H25.0845L27.7539 0.549805H32.8964L29.2849 28.0289H20.3345L16.8015 3.61176H16.0949L12.5619 28.0289H3.61154Z"
                  fill="black"/>
            <path d="M58.1105 26.2095C55.5273 26.2095 53.4724 25.6877 51.9459 24.644C50.4195 23.5859 49.6562 22.0784 49.6562 20.1216V16.4688C49.6562 14.512 50.4195 13.0117 51.9459 11.9681C53.4724 10.9099 55.5273 10.3809 58.1105 10.3809C60.6938 10.3809 62.7486 10.9099 64.2751 11.9681C65.8015 13.0117 66.5648 14.512 66.5648 16.4688V20.1216C66.5648 22.0784 65.8015 23.5859 64.2751 24.644C62.7486 25.6877 60.6938 26.2095 58.1105 26.2095Z"
                  fill="black"/>
            <path d="M44 0H57V4.64108H44V0Z" fill="black"/>
            <path d="M44 23.9375H57V28.5786H44V23.9375Z" fill="black"/>
            <path d="M36.1381 25.7519C38.1794 27.6361 40.9273 28.5783 44.3819 28.5783V23.9461C42.4714 23.9461 40.9666 23.3834 39.8674 22.2581C38.7944 21.1327 38.2579 19.6279 38.2579 17.7437V10.8346C38.2579 8.95034 38.7944 7.44553 39.8674 6.3202C40.9666 5.19486 42.4714 4.63219 44.3819 4.63219V0C40.9273 0 38.1794 0.955227 36.1381 2.86568C34.0968 4.74996 33.0762 7.45862 33.0762 10.9916V17.5866C33.0762 21.1197 34.0968 23.8414 36.1381 25.7519Z"
                  fill="black"/>
            <path d="M65.2437 2.82627C63.2024 0.941984 60.4545 -0.000158996 57 -0.000159298L57 4.63204C58.9104 4.63204 60.4152 5.1947 61.5144 6.32004C62.5874 7.44537 63.1239 8.95018 63.1239 10.8345L63.1239 17.7435C63.1239 19.6278 62.5874 21.1326 61.5144 22.2579C60.4152 23.3833 58.9104 23.9459 57 23.9459L57 28.5781C60.4545 28.5781 63.2024 27.6229 65.2437 25.7124C67.285 23.8282 68.3057 21.1195 68.3057 17.5865L68.3057 10.9915C68.3057 7.45846 67.285 4.73672 65.2437 2.82627Z"
                  fill="black"/>
            <path d="M95.1105 26.2095C92.5273 26.2095 90.4724 25.6877 88.9459 24.644C87.4195 23.5859 86.6562 22.0784 86.6562 20.1216V16.4688C86.6562 14.512 87.4195 13.0117 88.9459 11.9681C90.4724 10.9099 92.5273 10.3809 95.1105 10.3809C97.6938 10.3809 99.7486 10.9099 101.275 11.9681C102.802 13.0117 103.565 14.512 103.565 16.4688V20.1216C103.565 22.0784 102.802 23.5859 101.275 24.644C99.7486 25.6877 97.6938 26.2095 95.1105 26.2095Z"
                  fill="black"/>
            <path d="M81 0H94V4.64108H81V0Z" fill="black"/>
            <path d="M81 23.9375H94V28.5786H81V23.9375Z" fill="black"/>
            <path d="M73.1381 25.7519C75.1794 27.6361 77.9273 28.5783 81.3819 28.5783V23.9461C79.4714 23.9461 77.9666 23.3834 76.8674 22.2581C75.7944 21.1327 75.2579 19.6279 75.2579 17.7437V10.8346C75.2579 8.95034 75.7944 7.44553 76.8674 6.3202C77.9666 5.19486 79.4714 4.63219 81.3819 4.63219V0C77.9273 0 75.1794 0.955227 73.1381 2.86568C71.0968 4.74996 70.0762 7.45862 70.0762 10.9916V17.5866C70.0762 21.1197 71.0968 23.8414 73.1381 25.7519Z"
                  fill="black"/>
            <path d="M102.244 2.82627C100.202 0.941984 97.4545 -0.000158996 94 -0.000159298L94 4.63204C95.9104 4.63204 97.4152 5.1947 98.5144 6.32004C99.5874 7.44537 100.124 8.95018 100.124 10.8345L100.124 17.7435C100.124 19.6278 99.5874 21.1326 98.5144 22.2579C97.4152 23.3833 95.9104 23.9459 94 23.9459L94 28.5781C97.4545 28.5781 100.202 27.6229 102.244 25.7124C104.285 23.8282 105.306 21.1195 105.306 17.5865L105.306 10.9915C105.306 7.45846 104.285 4.73672 102.244 2.82627Z"
                  fill="black"/>
            <path d="M107.119 28.0289V0.549805H112.301V11.8948H122.507V0.549805H127.689V28.0289H122.507V16.6055H112.301V28.0289H107.119Z"
                  fill="black"/>
        </svg>
    </div>
    <div class="back-icon"></div>

</div>