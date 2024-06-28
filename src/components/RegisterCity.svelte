<script>
  import {onMount} from 'svelte';
  import {collection, doc, getDoc, setDoc} from 'firebase/firestore';
  import {auth, db} from '../firebase.js';
  import {nextStep} from "../stores/stepStore.js";
  import {tracking} from "../tracking.js";

  let loading = false;
  const BERLIN = 'berlin'
  const ANOTHER = 'another city'
  // let ipCity = undefined;
  let selectedCity = undefined;
  let selectedAreas = new Set();
  const areas = [
    'any',
    'Mitte',
    'Neukölln',
    'Kreuzberg',
    'Pankow',
    'Friedrichshain',
    'Charlottenburg',
    'Spandau',
    'Steglitz',
    'Schöneberg',
    'Gesundbrunnen',
    'Wilmersdorf',
    'Treptow',
    'Moabit',
    'Köpenick',
    'Tiergarten',
    'other berlin area',
    '📦 I’m Moving to Berlin Soon',
  ];
  const options = [BERLIN, ANOTHER];


  const toggleArea = (area) => {
    if (selectedAreas.has(area)) {
      selectedAreas.delete(area);
    } else if (selectedAreas.size < 3) {
      selectedAreas.add(area);
    }
    selectedAreas = new Set(selectedAreas);
  };

  let isGermany = false
  let selectedCityOption = undefined
  $: {
    if (selectedCity?.toLowerCase() === BERLIN) {
      selectedCityOption = BERLIN
    } else {
      selectedCityOption = ANOTHER
    }
  }

  const selectOption = (option) => {
    selectedCityOption = option;
    // selectedCity = selectedCityOption.toLowerCase() === BERLIN ? BERLIN : (ipCity || "")
    selectedCity = selectedCityOption.toLowerCase() === BERLIN ? BERLIN : ""
    selectedAreas = new Set()
    tracking.track("OnboardingCitySelectCityOption", {selectedCityOption, selectedCity});
  };

  const handleCityInput = (event) => {
    selectedCity = event.target.value;
  };

  onMount(async () => {
    tracking.track("OnboardingCityLoaded");
    loading = true;
    try {
      try {
        const response = await fetch("https://ipinfo.io/json?token=d2feb4f693903d");
        if (response.ok) {
          const data = await response.json();
          isGermany = data.country === 'DE';
          // ipCity = data.city
        } else {
          isGermany = false;
        }
      } catch {
        isGermany = false;
      }

      const docRef = doc(collection(db, 'users'), auth.currentUser.uid);
      const docSnap = await getDoc(docRef);

      if (docSnap.exists()) {
        if (docSnap.data().city) {
          selectedCity = docSnap.data().city;
        }
        selectedAreas = new Set(docSnap.data().areas || []);
      }
      if (selectedCity === BERLIN || (isGermany && !selectedCity)) {
        selectOption(BERLIN)
      } else if (!selectedCity) {
        selectOption(ANOTHER)
      }

    } catch (error) {
      tracking.track("OnboardingCityError", {error: JSON.stringify(error)});
    }
    loading = false;
  });

  const next = async () => {
    tracking.track("OnboardingCityNext", {selectedCity, areas});
    try {
      await setDoc(doc(collection(db, 'users'), auth.currentUser.uid), {
        city: selectedCity.toLowerCase(),
        areas: Array.from(selectedAreas)
      }, {merge: true});
      nextStep()
    } catch (error) {
      tracking.track("OnboardingCityError", {error: JSON.stringify(error)});
    }
  };
  $: buttonEnabled = selectedCity?.toLowerCase() === BERLIN ? selectedAreas.size > 0 : selectedCity?.length > 0

</script>


<div class="content-box">
    <form on:submit|preventDefault={next}>
        <div class="center">
            <div class="question-container">
                <div class="onboarding-h1">In which city are you looking for friends?</div>
                {#if selectedCity?.toLowerCase() === BERLIN}
                    <div class="radio-container">
                        {#each options as option}
                            <div class="radio-option" on:click={() => selectOption(option)}
                                 on:keypress={() => selectOption(option)}>
                                <div class="radio-icon">
                                    <div class="radio-icon-background {selectedCityOption === option ? 'selected': 'not-selected'}">
                                        {#if selectedCityOption === option }
                                            <svg width="12" height="10" viewBox="0 0 12 10" fill="none"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path
                                                        d="M4.89551 9.93628C4.5651 9.93628 4.28662 9.79704 4.06006 9.51855L1.17847 5.92896C1.08879 5.82039 1.02507 5.71655 0.987305 5.61743C0.949544 5.51359 0.930664 5.40739 0.930664 5.29883C0.930664 5.05811 1.0109 4.85986 1.17139 4.7041C1.33187 4.54362 1.53719 4.46338 1.78735 4.46338C2.06584 4.46338 2.29948 4.58374 2.48828 4.82446L4.86719 7.88306L9.46924 0.562256C9.5778 0.401774 9.68872 0.288493 9.802 0.222412C9.91528 0.151611 10.0569 0.116211 10.2268 0.116211C10.4722 0.116211 10.6729 0.194092 10.8286 0.349854C10.9891 0.500895 11.0693 0.696777 11.0693 0.9375C11.0693 1.0319 11.0528 1.12866 11.0198 1.22778C10.9915 1.3269 10.9419 1.43075 10.8711 1.53931L5.73096 9.49731C5.53271 9.78996 5.25423 9.93628 4.89551 9.93628Z"
                                                        fill="white"/>
                                            </svg>
                                        {/if}

                                    </div>
                                </div>
                                <div class="radio-label {selectedCityOption === option ? 'selected' : 'not-selected'}">
                                    {"in " + option}
                                </div>
                            </div>
                        {/each}
                    </div>
                {/if}
            </div>
            {#if selectedCityOption?.toLowerCase() === BERLIN}
                <div class="question-container area">
                    <div class="question">Choose 1-3 areas you want to meet in:</div>
                    <div class="option-box">
                        {#each areas as area}
                            <div on:click={() => toggleArea(area)} on:keypress={() => toggleArea(area)}
                                 class="option {selectedAreas.has(area) ? 'selected' : ''}">
                                <div class="option-text">{area}</div>
                            </div>
                        {/each}
                    </div>
                </div>
            {:else}
                <div class="input-container">
                    <div class="question">Enter the city</div>
                    <div class="input-box">
                        <div class="input-icon">📍</div>
                        <input type="text" placeholder="eg. Berlin" bind:value={selectedCity}
                               on:input={handleCityInput}
                               class="input" autofocus/>
                    </div>
                </div>
            {/if}


        </div>

        <button class="btn next-button" disabled={!buttonEnabled || loading}>next</button>
    </form>
</div>

<style>
    .radio-container {
        margin-top: 15px;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        gap: 18px;
    }

    .radio-option {
        display: flex;
        align-items: center;
        cursor: pointer;
    }

    .radio-icon {
        width: 24px;
        height: 22px;
        position: relative;
    }

    .radio-icon-background {
        width: 18px;
        height: 18px;
        color: white;
        border-radius: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .radio-icon-background.selected {
        background-color: black;
        border: 2px solid black;
    }

    .radio-icon-background.not-selected {
        border: 2px solid rgba(0, 0, 0, 0.50);
    }


    .radio-label {
        margin-left: 4px;
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.28px;
    }

    .radio-label.selected {
        color: black;
    }

    .radio-label.not-selected {
        color: rgba(0, 0, 0, 0.50);
    }

    .area {
        margin-top: 20px;
    }
</style>
