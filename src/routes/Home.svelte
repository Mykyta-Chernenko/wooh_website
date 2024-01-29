<script>
    import {navigate} from "svelte-routing";
    import PainBlock from "../components/PainBlock.svelte";
    import AlternativeBlock from "../components/AlternativeBlock.svelte";
    import DifferenceBlock from "../components/DifferenceBlock.svelte";
    import {tracking} from "../tracking.js";
    import {onMount, tick} from "svelte";

    export let inviteCode;
    let city; // city is undefined until we retrieve the location

    let activeTab = 'pain'
    onMount(async () => {
        //     function resize() {
        //         var baseWidth = 1440;
        //         var scaleFactor = window.innerWidth / baseWidth;
        //         document.documentElement.style.zoom = scaleFactor;
        //     }
        //
        //     // Event listener for resizing the window
        //     window.addEventListener('resize', resize);
        //
        //     // Initial resize when the document loads
        //     document.addEventListener('DOMContentLoaded', resize);
        //
        const response = await fetch("https://ipinfo.io/json?token=d2feb4f693903d");
        if (response.ok) {
            const data = await response.json();
            if (data.country === 'DE') {
                city = "Berlin"
            } else {
                city = "your city";
            }
        } else {
            city = "your city";
        }
        tracking.track("HomeLoaded", {city, inviteCode});
        await tick()

        const observerCallback = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    activeTab = entry.target.id;
                    tracking.track("HomeActiveTabChange", {activeTab});
                }
            });
        };

        const observerOptions = {
            root: null,
            threshold: 0.2,
        };
        const observer = new IntersectionObserver(observerCallback, observerOptions);


        const targets = ['pain', 'alternative', 'difference'].map(id => document.getElementById(id));

        targets.forEach(target => {
            if (target) observer.observe(target);
        });

        return () => {
            targets.forEach(target => {
                if (target) observer.unobserve(target);
            });
        };
    });

    function scrollIntoView({target}) {
        tracking.track("HomeMenuClicked", {target: target.getAttribute('href')});
        const el = document.querySelector(target.getAttribute('href'));
        if (!el) return;
        activeTab = el.id;
        el.scrollIntoView({
            behavior: 'smooth'
        });
    }


    function goToRegister() {
        tracking.track("HomeSignUpClicked");
        if (inviteCode) {
            navigate("/register?invite_code=" + inviteCode);
        } else {
            navigate("/register");
        }
    }

</script>

{#if city}
    <div class="sticky-header">
        <svg xmlns="http://www.w3.org/2000/svg" width="129" height="42" viewBox="0 0 129 42" fill="none">
            <path d="M45.8198 34.6946C51.6914 37.6622 59.2022 39.0099 69.8689 39.0099C80.5356 39.0099 88.0464 37.6622 93.918 34.6946"
                  stroke="black" stroke-width="5"/>
            <path d="M4.34543 28.0287L0.733887 0.549561H5.87641L8.54581 24.4171H9.25241L12.7069 0.549561H21.6573L25.1118 24.4171H25.8184L28.4878 0.549561H33.6303L30.0188 28.0287H21.0684L17.5354 3.61152H16.8288L13.2958 28.0287H4.34543Z"
                  fill="black"/>
            <path d="M58.8444 26.2097C56.2612 26.2097 54.2063 25.6879 52.6798 24.6443C51.1534 23.5861 50.3901 22.0786 50.3901 20.1218V16.469C50.3901 14.5122 51.1534 13.012 52.6798 11.9683C54.2063 10.9102 56.2612 10.3811 58.8444 10.3811C61.4276 10.3811 63.4825 10.9102 65.009 11.9683C66.5354 13.012 67.2987 14.5122 67.2987 16.469V20.1218C67.2987 22.0786 66.5354 23.5861 65.009 24.6443C63.4825 25.6879 61.4276 26.2097 58.8444 26.2097Z"
                  fill="black"/>
            <path d="M44.7339 0H57.7339V4.64108H44.7339V0Z" fill="black"/>
            <path d="M44.7339 23.9373H57.7339V28.5783H44.7339V23.9373Z" fill="black"/>
            <path d="M36.872 25.7519C38.9133 27.6361 41.6612 28.5783 45.1158 28.5783V23.9461C43.2053 23.9461 41.7005 23.3834 40.6013 22.2581C39.5283 21.1327 38.9918 19.6279 38.9918 17.7437V10.8346C38.9918 8.95034 39.5283 7.44553 40.6013 6.3202C41.7005 5.19486 43.2053 4.63219 45.1158 4.63219V0C41.6612 0 38.9133 0.955227 36.872 2.86568C34.8307 4.74996 33.8101 7.45862 33.8101 10.9916V17.5866C33.8101 21.1197 34.8307 23.8414 36.872 25.7519Z"
                  fill="black"/>
            <path d="M65.9776 2.82651C63.9363 0.942228 61.1884 8.51443e-05 57.7339 8.48423e-05L57.7339 4.63228C59.6443 4.63228 61.1491 5.19495 62.2483 6.32028C63.3213 7.44562 63.8578 8.95043 63.8578 10.8347L63.8578 17.7437C63.8578 19.628 63.3213 21.1328 62.2483 22.2582C61.1491 23.3835 59.6443 23.9462 57.7339 23.9462L57.7339 28.5784C61.1884 28.5784 63.9363 27.6231 65.9776 25.7127C68.0189 23.8284 69.0396 21.1198 69.0396 17.5867L69.0396 10.9917C69.0396 7.4587 68.0189 4.73697 65.9776 2.82651Z"
                  fill="black"/>
            <path d="M95.8444 26.2097C93.2612 26.2097 91.2063 25.6879 89.6798 24.6443C88.1534 23.5861 87.3901 22.0786 87.3901 20.1218V16.469C87.3901 14.5122 88.1534 13.012 89.6798 11.9683C91.2063 10.9102 93.2612 10.3811 95.8444 10.3811C98.4276 10.3811 100.483 10.9102 102.009 11.9683C103.535 13.012 104.299 14.5122 104.299 16.469V20.1218C104.299 22.0786 103.535 23.5861 102.009 24.6443C100.483 25.6879 98.4276 26.2097 95.8444 26.2097Z"
                  fill="black"/>
            <path d="M81.7339 0H94.7339V4.64108H81.7339V0Z" fill="black"/>
            <path d="M81.7339 23.9373H94.7339V28.5783H81.7339V23.9373Z" fill="black"/>
            <path d="M73.872 25.7519C75.9133 27.6361 78.6612 28.5783 82.1158 28.5783V23.9461C80.2053 23.9461 78.7005 23.3834 77.6013 22.2581C76.5283 21.1327 75.9918 19.6279 75.9918 17.7437V10.8346C75.9918 8.95034 76.5283 7.44553 77.6013 6.3202C78.7005 5.19486 80.2053 4.63219 82.1158 4.63219V0C78.6612 0 75.9133 0.955227 73.872 2.86568C71.8307 4.74996 70.8101 7.45862 70.8101 10.9916V17.5866C70.8101 21.1197 71.8307 23.8414 73.872 25.7519Z"
                  fill="black"/>
            <path d="M102.978 2.82651C100.936 0.942228 98.1884 8.51443e-05 94.7339 8.48423e-05L94.7339 4.63228C96.6443 4.63228 98.1491 5.19495 99.2483 6.32028C100.321 7.44562 100.858 8.95043 100.858 10.8347L100.858 17.7437C100.858 19.628 100.321 21.1328 99.2483 22.2582C98.1491 23.3835 96.6443 23.9462 94.7339 23.9462L94.7339 28.5784C98.1884 28.5784 100.936 27.6231 102.978 25.7127C105.019 23.8284 106.04 21.1198 106.04 17.5867L106.04 10.9917C106.04 7.4587 105.019 4.73697 102.978 2.82651Z"
                  fill="black"/>
            <path d="M107.853 28.0287V0.549561H113.035V11.8945H123.241V0.549561H128.423V28.0287H123.241V16.6052H113.035V28.0287H107.853Z"
                  fill="black"/>
        </svg>
        <div class="navigation">
            <a href="#pain" class="nav-item" class:active="{activeTab==='pain'}"
               on:click|preventDefault={scrollIntoView}>pain</a>
            <a href="#alternative" class="nav-item" class:active="{activeTab==='alternative'}"
               on:click|preventDefault={scrollIntoView}>alternative</a>
            <a href="#difference" class="nav-item" class:active="{activeTab==='difference'}"
               on:click|preventDefault={scrollIntoView}>difference</a>
        </div>
        <div class="header-btn">
            <button class="btn" on:click={goToRegister}>sign up</button>
        </div>
    </div>
    <div class="content-wrapper">
        <div class="header-block-wrapper">
            <div class="tag-container">
                <div class="tag" style="background: #FBE3E3; border-color: #F9D0D0;">No Swipes</div>
                <div class="tag" style="background: #C4E5FF; border-color: #99CFF9;">Only IRL Meetings</div>
                <div class="tag" style="background: #CCC4FF; border-color: #A693F3;">Expat Community</div>
                <div class="tag" style="background: #CEF7CF; border-color: #8FDB91;">1 Person per Week</div>
            </div>
            <h1>Find your Local International Friends in {city}</h1>
            <button class="btn" on:click={goToRegister}>sign up</button>
            <div class="grey-text">Launching soon</div>
        </div>
        <div class="header-image-wrapper">
            <img src="/assets/images/header_banner.png" alt="phone with notification to meet a friend"/>
        </div>

        <PainBlock></PainBlock>
        <AlternativeBlock></AlternativeBlock>
        <DifferenceBlock></DifferenceBlock>

        <div class="footer">
            <div class="footer-bg-1"></div>
            <div class="footer-bg-2"></div>
            <div class="footer-bg-3"></div>
            <div class="footer-conter">
                <div class="tag-container" style="margin: 0 -10px">
                    <div class="tag" style="background: #FBE3E3; border-color: #F9D0D0;">No Swipes</div>
                    <div class="tag" style="background: #C4E5FF; border-color: #99CFF9;">Only IRL Meetings</div>
                    <div class="tag" style="background: #CCC4FF; border-color: #A693F3;">Expat Community</div>
                    <div class="tag" style="background: #CEF7CF; border-color: #8FDB91;">1 Person per Week</div>
                </div>
                <h1 class="footer-title">Ready to Find New International Friends in {city}?</h1>
                <button class="btn" on:click={goToRegister}>sign up</button>
            </div>
        </div>

    </div>


{/if}

<style>
    .sticky-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: rgba(0, 0, 0, 0);
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 10;
        margin: 2vh;
        height: 5vh;
    }

    .navigation {
        background-color: #EBEBEB;
        padding: 4px;
        gap: 10px;
        border-radius: 8px;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    @media (max-width: 1038px) {
        .navigation {
            display: none
        }
    }

    @media (max-width: 1038px) {
        .header-btn {
            display: none;
        }
    }

    .nav-item {
        display: flex;
        padding: 6px 30px;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
        cursor: pointer;
        text-transform: uppercase;
    }

    .nav-item.active {
        border: 1px solid #DDD;
        background: #FFF;
    }


    .tag {
        min-width: 100px;
        padding: 8px 16px;
        border-radius: 8px;
        border: 1px solid;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .tag-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
    }

    .tag:nth-child(odd) {
        transform: rotate(3deg);
    }

    .tag:nth-child(even) {
        transform: rotate(-3deg);
    }


    .content-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 1038px;
        margin-top: 15vh;
    }

    .header-image-wrapper {
        margin-top: 7vh;
        display: flex;
        border-radius: 32px;
        flex-direction: column;
        align-items: center;
    }

    .header-block-wrapper {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: center;
        justify-content: center;
    }

    .header-image-wrapper img {
        width: 100%;
    }


    .footer {
        transform: rotate(0.994deg);
        position: relative;
        margin: 10vh 0;
        display: flex;
        max-width: 1336px;

    }

    .footer-title {
        margin: 3vh 1vw;
        max-width: 70%;
    }

    .footer-conter {
        z-index: 1;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20vh 10px;
        box-sizing: border-box;
        border-radius: 30px;
        background-color: white;
    }

    .footer-bg-1 {
        position: absolute;
        width: 100%;
        height: 100%;
        border: 0.647px solid #FFF;
        transform: rotate(-0.5deg);
        background: rgba(255, 255, 255, 0.17);
        border-radius: 30px;
        z-index: -1;
    }

    .footer-bg-2 {
        position: absolute;
        width: 100%;
        height: 100%;
        transform: rotate(-1.316deg);
        background: linear-gradient(0deg, #C4BCF5 0%, #C4BCF5 100%);
        border-radius: 30px;
        z-index: -2;
    }

    .footer-bg-3 {
        position: absolute;
        width: 100%;
        height: 100%;
        transform: rotate(2.52deg);
        border: 0.647px solid #FFF;
        background: #FBE3E3;
        border-radius: 30px;
        z-index: -3;
    }

    .grey-text {
        margin-top: 8px;
        color: rgba(0, 0, 0, 0.35);
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        word-wrap: break-word
    }


    @media (max-width: 600px) {
        .header-image-wrapper img {
            width: 95vw;
        }
        .footer {
            width: 95vw;
        }

        .footer-conter {
            padding: 10vh 10px;
        }

        .footer-title {
            max-width: 100%;
            margin: 2vh 0;
        }
    }

</style>
