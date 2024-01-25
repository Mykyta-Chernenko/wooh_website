<script>
    import {step, TOTAL_STEPS} from '../stores/stepStore';
</script>
<style>
    .progress {
        width: 100%;
        background-color: #D9D9D9;
        height: 4px;
        margin-bottom: 10%;
    }

    .progress-filled {
        height: 4px;
        background-color: black;
    }
</style>
{#if $step !== 0}
    <div class="progress">
        <div class="progress-filled" style="width: {$step/(TOTAL_STEPS+1)*100}%">
        </div>
    </div>
{/if}