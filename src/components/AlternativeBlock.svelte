<script>
  // Svelte script logic (if any)
</script>

<div class="block-container" id="alternative">
  <div class="block-tag">
    <div class="text uppercase">Alternative</div>
  </div>
  <h1>How about WOOH Way?</h1>

  <div class="process-container">
    <div class="process-step" style="background:#C9F8CA ">
      <div class="step">1</div>
      <div class="step-title">Share who you are.</div>
      <div class="step-description">
        Share your interests in a way that a photo never could. Let your values
        do the talking.
      </div>
      <div class="blur"></div>
      <div class="floating-text first">☘️ Values</div>
      <div class="floating-text second">🎵️ Passions</div>
      <div class="floating-text third">✏️ Personality</div>
    </div>
    <div class="process-step" style="background: #C1E9FF;">
      <div class="step">2</div>
      <div class="step-title">Once per week get only 1 new friend to meet.</div>
      <div class="step-description">
        Each week, you get 1 tailored friend based on your values, without
        countless swipes.
      </div>
      <div class="blur"></div>
      <div class="floating-text first">Your new<br />weekly friend</div>
      <div
        class="floating-text second"
        style="font-size: 28px; padding: 5px; transform: rotate(5deg)"
      >
        ‍🧑🏾‍🦰
      </div>
      <div class="floating-text third">Meet Mykyta</div>
    </div>

    <!-- New block for step 3 -->
    <div class="process-step" style="background: #FBE3E3;">
      <div class="step">3</div>
      <div class="step-title">Set the time and place to meet.</div>
      <div class="step-description">
        Choose time and place where you both would like to meet.
      </div>
      <img
        class="process-img"
        src="/assets/images/calendar.png"
        alt="calendar"
      />
      <!-- Additional elements like date cards can be added here -->
    </div>

    <!-- New block for step 4 -->
    <div class="process-step" style="background: #C4BCF5;">
      <div class="step">4</div>
      <div class="step-title">
        Meet in real life and and explore the possibility of friendship.
      </div>
      <div class="step-description">
        Friendship is about shared moments, not just shared texts. Have Fun!
      </div>
      <div class="blur"></div>
      <div class="floating-text first">💫 connect</div>
      <div class="floating-text second">🙃️ have fun</div>
      <div class="floating-text third">️🧑🏽‍🦱 get friend</div>
    </div>
  </div>
</div>

<style>
  .block-container {
    margin-top: 10vh;
    padding: 20px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  @media (max-width: 600px) {
    .block-container {
      margin-top: 0;
    }
  }

  .block-tag {
    background: white;
    border-radius: 8px;
    border: 1px solid #dddddd;
    padding: 8px 16px;
    margin-top: 3vh;
    font-weight: 500;
  }

  .process-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 20px;
    justify-content: center;
  }

  .process-step {
    position: relative;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 20px;
    box-sizing: border-box;
    overflow: hidden;
    width: 100%;
    height: 100%;
  }

  @media (min-width: 601px) {
    .process-container {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 600px) {
    .process-container {
      grid-template-columns: repeat(1, 1fr);
    }
  }

  .step {
    border-radius: 100px;
    height: 30px;
    width: 30px;
    background-color: black;
    color: #c9f8ca;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
  }

  .step-title {
    font-size: 32px;
    line-height: 36px;
    font-weight: 500;
  }
  @media (max-width: 600px) {
    .step-title {
      font-size: 28px;
      line-height: 30px;
    }
  }

  .step-description {
    max-width: 80%;
    color: rgba(0, 0, 0, 0.6);
    font-weight: 500;
    font-size: 16px;
    margin-bottom: 50%;
  }

  .blur {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 60%;
    left: 40%;
    transform: rotate(-6.06deg);
    background: rgba(255, 255, 255, 0.17);
    box-shadow: 0 2.5899996757507324px 38.849998474121094px
      rgba(24, 24, 24, 0.04);
    border-radius: 20px;
    border: 0.65px solid white;
    backdrop-filter: blur(9.9px);
  }

  .process-img {
    position: absolute;
    bottom: 0;
    right: 0;
    height: 50%;
  }

  .floating-text {
    position: absolute;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    border: 0.65px solid white;
    backdrop-filter: blur(9.9px);
    box-shadow: 0 2.59px 38.85px rgba(24, 24, 24, 0.04);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    text-transform: uppercase;
    font-family: "Space Grotesk", sans-serif;
    font-weight: 500;
    font-size: 14px;
  }

  .first {
    bottom: 5%;
    right: -1%;
    transform: rotate(-15deg);
  }

  .second {
    bottom: 33%;
    right: 2%;
    transform: rotate(-15deg);
  }

  .third {
    bottom: 14%;
    right: 40%;
    transform: rotate(3deg);
  }

  @media (max-width: 600px) {
    .process-step {
      width: 95vw;
    }
  }
</style>
