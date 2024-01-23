<script>
    // Add script logic here if necessary
</script>

<style>
    .intro {
        width: 100%;
        height: 100vh;
        position: relative;
        background: #F5F5F5;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 60px 0;
    }

    .group49 {
        max-width: 335px;
        width: 100%;
        position: relative;
        text-align: center;
    }

    .welcome-text {
        font-size: 40px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        line-height: 1;
        margin: 0;
        color: black;
        word-wrap: break-word;
    }

    .time-frame {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background: white;
        border-radius: 8px;
        border: 1px solid #DDDDDD;
        margin-top: 20px;
        padding: 8px 16px;
    }

    .time-text {
        color: black;
        font-size: 14px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        word-wrap: break-word;
    }

    .info-box {
        background: #C4E5FF;
        border-radius: 12px;
        border: 1px solid #99CFF9;
        padding: 20px 16px;
        display: flex;
        gap: 8px;
        align-items: center;
        margin-top: 40px;
    }

    .info-text {
        color: black;
        font-size: 13px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        line-height: 16px;
        letter-spacing: 0.26px;
        word-wrap: break-word;
    }

    .start-button {
        background: black;
        color: white;
        border-radius: 8px;
        padding: 16px 30px;
        font-size: 14px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
        margin-top: 20px;
        cursor: pointer;
    }

    @media (max-width: 768px) {
        .intro {
            padding: 60px 20px;
        }

        .group49 {
            width: calc(100% - 40px);
        }

        .welcome-text {
            font-size: 30px;
        }

        .time-frame {
            margin-top: 15px;
        }

        .info-box {
            padding: 20px;
        }

        .start-button {
            padding: 16px;
        }
    }
</style>

<div class="intro">
    <div class="group49">
        <p class="welcome-text">👋 Hi! We have 10 questions for you before you join</p>
        <div class="time-frame">
            <span class="time-text">3 minutes to fill</span>
        </div>
        <div class="info-box">
            <div class="info-icon">Icon</div>
            <p class="info-text">Your answers help us to make value-based match with your new friends.</p>
        </div>
        <button class="start-button">let’s start</button>
    </div>
</div>
