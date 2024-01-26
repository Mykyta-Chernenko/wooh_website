import App from "./App.svelte";
import {tracking} from './tracking'

tracking.track('SessionStart')

const app = new App({
    target: document.body,
});

export default app;
