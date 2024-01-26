<script>
    // Svelte script logic (if any)
</script>

<div class="block-container" id="pain">
    <div class="tag">
        <div class="text">relocation Pain</div>
    </div>
    <h1>Do you know the
        <span class="pain-tag">
           pain
        </span>
        of relocating? Leaving Friends behind hits hard!
    </h1>
    <div class="info-section">
        <div class="info-card">
            <div class="emoji">😩</div>
            <div class="text">silent weekends?</div>
        </div>
        <div class="info-card">
            <div class="emoji">👽</div>
            <div class="text">hard to connect with locals?</div>
        </div>
        <div class="info-card">
            <div class="emoji">🚴‍♀️</div>
            <div class="text">doing activities alone?</div>
        </div>
        <div class="info-card">
            <div class="emoji">🍻</div>
            <div class="text">no beer buddies?</div>
        </div>
        <div class="info-card">
            <div class="emoji">🎉</div>
            <div class="text">no birthday parties?</div>
        </div>
        <div class="info-card">
            <div class="emoji">🧐</div>
            <div class="text">no deep conversations?</div>
        </div>
    </div>
    <div class="highlight-block">
        <h1>
            And above all, searching for friends in a new city <span class="nowhere-tag">leads nowhere</span>? We know!
        </h1>
        <div class="emoji-bottom one">🔦</div>
        <div class="emoji-bottom two">👀</div>
        <div class="emoji-bottom three">🔍</div>
    </div>
</div>

<style>
    .block-container {
        margin-top: 5vh;
        border-radius: 32px;
        background: white;
        padding: 20px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
    }


    .pain-tag {
        z-index: -1;
        display: inline-block;
        background: #FBE3E3;
        border-radius: 8px;
        border: 1px solid #F9D0D0;
        padding: 2px 1px;
        margin: -6px 0;
        rotate: -1deg;
    }

    .tag {
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        padding: 8px 16px;
        margin-top: 3vh;
    }

    .info-section {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 20px;
        justify-content: center;
    }

    @media (min-width: 601px) {
        .info-section {
            grid-template-columns: repeat(3, 1fr);
        }
    }

    @media (max-width: 600px) {
        .info-section {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    .info-card {
        flex-basis: calc(33.333% - 20px);
        max-width: 200px;
        padding: 30px 10px;
        background: #F5F5F5;
        border-radius: 16px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        box-sizing: border-box;
        text-align: center;
    }

    .emoji {
        font-size: 46px;
    }

    .text {
        font-size: 14px;
        text-transform: uppercase;
        word-wrap: break-word;
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 10px;
            max-width: 100%;
        }


        .info-card {
            flex-basis: calc(50% - 20px);
        }

        .info-section {
            gap: 10px;
        }
    }

    @media (max-width: 480px) {
        .info-card {
            flex-basis: 100%;
        }
    }

    .highlight-block {
        margin-top: 7vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        margin-bottom: 15vh;
    }


    .nowhere-tag {
        display: inline-block;
        background: #C4E5FF;
        border-radius: 8px;
        border: 1px solid #99CFF9;
        padding: 0px 1px;
        margin: -6px 0;
        z-index: -1;
        rotate: -1deg;
    }

    .emoji-bottom {
        font-size: 3rem;
        position: absolute;
    }


    /* Positioning the emojis based on the image */
    .emoji-bottom.one { /* Assuming this is the flashlight emoji */
        top: -3rem;
        right: 1rem;
    }

    .emoji-bottom.two { /* Assuming this is the eyes emoji */
        top: -2rem;
        left: 2rem;
    }

    .emoji-bottom.three { /* Assuming this is the magnifying glass emoji */
        bottom: -5rem;
        left: 30%;
    }

</style>

