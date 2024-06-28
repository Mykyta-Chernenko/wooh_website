<script>
  let deferredPrompt;
  let showButton = true;

  // const showInstallPrompt = async () => {
  //   if (window.deferredInstallPrompt) {
  //     await window.deferredInstallPrompt.prompt()
  //     window.deferredInstallPrompt = null
  //     showButton = true;
  //   }
  // }
  // window.addEventListener('beforeinstallprompt', (e) => {
  //   console.log('here')
  //   // Prevent the mini-infobar from appearing on mobile
  //   e.preventDefault();
  //   // Stash the event so it can be triggered later.
  //   deferredPrompt = e;
  //   // Show the install button
  //   showButton = true;
  // });

  async function installPWA() {
    // if (!deferredPrompt) return;
    // Show the install prompt
    window.deferredInstallPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') {
      console.log('User accepted the install prompt');
    } else {
      console.log('User dismissed the install prompt');
    }
    // Hide the button after prompt
    showButton = false;
    deferredPrompt = null;
  }
</script>

{#if showButton}
    <button on:click={installPWA}>Install</button>
{/if}
