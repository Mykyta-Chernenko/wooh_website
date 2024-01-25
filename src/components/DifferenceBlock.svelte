<script>
    // Svelte script logic (if any)
</script>

<div class="block-container" id="difference">
    <div class="block-tag">
        <div class="text">Difference</div>
    </div>
    <h1>A Fresh Take on Finding Friends</h1>

    <div class="card-container">
        <h2><span class="tag red">Locals</span> are hard to connect with?</h2>
        <img class="first-image" style="margin:20px" src="/assets/images/random_people.png" alt="random people">
        <h2 class="second-text">We are a <span class="tag purple">community</span> of Expats in Berlin, who are open to friendship.</h2>
    </div>
    <div class="card-container">
        <h2>Annoyed with <span class="tag red">Endless Swipes</span>?</h2>
        <img class="second-image" style="margin:20px" src="/assets/images/weekly_match.png" alt="weekly match">
        <h2 class="second-text">Get only <span class="tag green">1 tailored friend</span> per week.</h2>
    </div>
    <div class="card-container">
        <h2>Annoyed with <span class="tag red">Matching by Photo?</span></h2>
        <div class="profile-card">
            <div class="emoji-container">🧑🏽‍🦱</div>
            <h2 class="profile-question">Do you want to Meet with Daniel?</h2>
            <p class="profile-origin">from 🇪🇸 Spain</p>
            <button class="action-button">Yes, continue</button>
        </div>
        <h2 class="second-text">See Friend’s photo only after both of you accepted each other's <span class="tag purple">Values</span>.</h2>
    </div>
    <div class="card-container">
        <h2>Tired of <span class="tag red">Empty Chats</span></h2>
        <img class="third-image" style="margin:20px" src="/assets/images/process.png" alt="weekly match">
        <h2 class="second-text">We skip chatting, you can only <span class="tag blue">meet IRL</span>.</h2>
    </div>

</div>

<style>
    .block-container {
        margin-top: 10vh;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
    }

    .block-tag {
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        padding: 8px 16px;
        margin-top: 3vh;
    }

    .tag {
        display: inline-block;
        background: #FBE3E3;
        border-radius: 8px;
        border: 1px solid #F9D0D0;
        padding: 2px 1px;
        margin: -6px 0;
        z-index: -1;
        rotate: -1deg;
    }

    .tag {
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        padding: 8px 16px;
        margin-top: 3vh;
    }

    .card-container {
        width: 100%;
        max-width: 1038px;
        padding: 10vh 20px;
        background: white;
        border-radius: 32px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
        text-align: center;
        margin-bottom: 5vh;

    }

    .profile-card {
        width: 306px;
        border: 1px solid #DDDDDD;
        border-radius: 16px;
        display: flex;
        flex-direction: column;
        text-align: center;
        align-items: center;
        justify-content: center;
        padding: 20px;
        margin: 5vh 0;
    }

    .profile-question {
        color: black;
        font-size: 1.4rem;
        line-height: 1.4rem;
        max-width: 70%;
        text-align: center;
    }

    .profile-origin {
        color: black;
        text-transform: uppercase;
    }

    .action-button {
        background: #F5F5F5;
        border-radius: 8px;
        color: black;
        text-transform: uppercase;
        padding: 11px 30px;
        border: none;
        margin-top: 20px;
    }

    .emoji-container {
        color: black;
        font-size: 56px;
        font-weight: 500;
        text-transform: uppercase;
        padding: 15.5px 23px;
        border-radius: 20px;
    }

    .tag {
        display: inline-block;
        border-radius: 8px;
        padding: 2px 1px;
        margin: -6px 0;
        rotate: -1deg;
    }

    .tag.blue {
        background: #C4E5FF;
        border: 1px solid #99CFF9;
    }

    .tag.red {
        background: #FBE3E3;
        border: 1px solid #F9D0D0;
    }

    .tag.purple {
        background: #CCC4FF;
        border: 1px solid #A693F3;
    }

    .tag.green {
        background: #CEF7CF;
        border: 1px solid #8FDB91;
    }
    .second-image{
        width: 60%;
    }
    @media (max-width: 600px) {
        .second-image {
            width: 100%;
        }
    }
    .first-image{
        width: 80%;
    }
    @media (max-width: 600px) {
        .first-image {
            width: 100%;
        }
    }

    .third-image{
        width: 70%;
    }
    @media (max-width: 600px) {
        .third-image {
            width: 100%;
        }
    }
    @media (min-width: 600px) {
        .second-text {
            width: 70%;
        }
    }

</style>

