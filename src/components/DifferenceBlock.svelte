<script>
    // Svelte script logic (if any)
</script>

<div class="block-container" id="difference">
    <div class="block-tag">
        <div class="text uppercase">Difference</div>
    </div>
    <h1>A Fresh Approach on Finding Friends</h1>

    <div class="card-container">
        <h2><span class="difference-tag red">Locals</span> are hard to connect with?</h2>
        <img class="first-image" style="margin:20px" src="/assets/images/random_people.png" alt="random people">
        <h2 class="second-text">We are a <span class="difference-tag purple">community</span> of Expats in Berlin, who are open to
            friendship.</h2>
    </div>
    <div class="card-container">
        <h2>Annoyed with <span class="difference-tag red">Endless Swipes</span>?</h2>
        <img class="second-image" style="margin:20px" src="/assets/images/weekly_match.png" alt="weekly match">
        <h2 class="second-text">Get only <span class="difference-tag green">1 new friend</span> per week to meet based on your
            Interests.</h2>
    </div>
    <div class="card-container">
        <h2>Annoyed with <span class="difference-tag red">Matching by Photo?</span></h2>
        <img class="third-image" style="margin:20px" src="/assets/images/value_match.png" alt="weekly match">
        <h2 class="second-text">See Friend’s photo only after both of you accepted each other's <span
                class="difference-tag purple">Values</span>.</h2>
    </div>
    <div class="card-container">
        <h2>Tired of <span class="difference-tag red">Empty Chats</span></h2>
        <img class="forth-image" style="margin:20px" src="/assets/images/process.png" alt="weekly match">
        <h2 class="second-text">We skip chatting, you can only <span class="difference-tag blue">meet IRL</span>.</h2>
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

    @media (max-width: 600px) {
        .block-container {
            margin-top: 0;
        }
    }

    .block-tag {
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        padding: 8px 16px;
        margin-top: 3vh;
        font-weight: 500;
    }

    .difference-tag {
        display: inline-block;
        background: #FBE3E3;
        border-radius: 8px;
        border: 1px solid #F9D0D0;
        padding: 2px 1px;
        margin: -6px 0;
        z-index: -1;
        rotate: -1deg;
    }

    .difference-tag {
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

    @media (max-width: 600px) {
        .card-container {
            margin-bottom: 10px;
        }
    }

    .difference-tag {
        display: inline-block;
        border-radius: 8px;
        padding: 2px 1px;
        margin: -6px 0;
        rotate: -1deg;
    }

    .difference-tag.blue {
        background: #C4E5FF;
        border: 1px solid #99CFF9;
    }

    .difference-tag.red {
        background: #FBE3E3;
        border: 1px solid #F9D0D0;
    }

    .difference-tag.purple {
        background: #CCC4FF;
        border: 1px solid #A693F3;
    }

    .difference-tag.green {
        background: #CEF7CF;
        border: 1px solid #8FDB91;
    }

    .first-image {
        width: 40%;
    }

    @media (max-width: 600px) {
        .first-image {
            width: 70%;
        }
    }

    .second-image {
        width: 30%;
    }

    @media (max-width: 600px) {
        .second-image {
            width: 60%;
        }
    }


    .third-image {
        width: 30%;
    }

    @media (max-width: 600px) {
        .third-image {
            width: 60%;
        }
    }

    .forth-image {
        width: 70%;
    }

    @media (max-width: 600px) {
        .forth-image {
            width: 100%;
        }
    }

    @media (min-width: 600px) {
        .second-text {
            width: 70%;
        }
    }

</style>

