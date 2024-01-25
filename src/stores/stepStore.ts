import {writable} from 'svelte/store';

export const step = writable(0);

export function nextStep() {
    step.update((step) => step + 1);
}

export const TOTAL_STEPS = 8;
