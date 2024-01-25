<script>
    import {nextStep} from "../stores/stepStore.js";
</script>

<style>

    .welcome-text {
        margin-top: 20px;
    }

    .time-frame {
        max-width: 158px;
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        padding: 8px 16px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        color: black;
    }

    .info-box {
        background: #C4E5FF;
        border-radius: 12px;
        border: 1px solid #99CFF9;
        padding: 20px 16px;
        font-size: 13px;
        font-weight: 500;
        color: black;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 30px;
        line-height: 16px;
        letter-spacing: 0.26px;
    }

    .icon {
        height: 32px;
        width: 32px;
    }


    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: start;
    }
</style>

<div class="content-box">
    <div></div>
    <div class="center">
        <div class="time-frame">4 minutes to fill</div>
        <div class="welcome-text onboarding-h1 center-text">👋 Hi! We have 8 questions for you before you join</div>
        <button class="btn next-button" on:click={nextStep}>let's start</button>
    </div>
    <div class="info-box">
        <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                <path d="M4 14H5.33333M16 2V3.33333M26.6667 14H28M7.46667 5.46667L8.4 6.4M24.5333 5.46667L23.6 6.4"
                      stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12.0007 19.3335C10.8813 18.494 10.0544 17.3235 9.63723 15.9879C9.22003 14.6524 9.23362 13.2194 9.6761 11.892C10.1186 10.5646 10.9675 9.41002 12.1026 8.59188C13.2377 7.77375 14.6014 7.3335 16.0007 7.3335C17.3999 7.3335 18.7636 7.77375 19.8987 8.59188C21.0338 9.41002 21.8827 10.5646 22.3252 11.892C22.7677 13.2194 22.7813 14.6524 22.3641 15.9879C21.9469 17.3235 21.12 18.494 20.0007 19.3335C19.4801 19.8488 19.0881 20.4794 18.8565 21.1743C18.6248 21.8692 18.56 22.6089 18.6673 23.3335C18.6673 24.0407 18.3864 24.719 17.8863 25.2191C17.3862 25.7192 16.7079 26.0002 16.0007 26.0002C15.2934 26.0002 14.6151 25.7192 14.115 25.2191C13.6149 24.719 13.334 24.0407 13.334 23.3335C13.4413 22.6089 13.3765 21.8692 13.1448 21.1743C12.9132 20.4794 12.5212 19.8488 12.0007 19.3335Z"
                      stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12.9336 20.6665H19.0669" stroke="black" stroke-width="1.5" stroke-linecap="round"
                      stroke-linejoin="round"/>
            </svg>
        </div>
        <div>Your answers help us to make value-based match with your new friends.</div>
    </div>
</div>
