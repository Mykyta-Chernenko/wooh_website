import {writable} from 'svelte/store';
import {tracking} from "../tracking";
import {auth} from "../firebase";

export const step = writable(0);

export function nextStep() {
    step.update((step) => {
        tracking.track("OnboardingNextStep", {stepTo: step + 1});
        return step + 1
    });
}

export async function signOut() {
    tracking.track("SignOut");
    tracking.reset();
    tracking.identify(tracking.get_distinct_id());
    await auth.signOut();
}

export const TOTAL_STEPS = 8;
