<svelte:head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript" on:load={plotlyLoaded}></script>
</svelte:head>

<script>
  import { onMount } from 'svelte';

  import Keypad from "./Keypad.svelte";

  let value = [];
  let counts = {};

  let plot;
  let plot2;

  let runs = 0;

  $: fetch('./runs', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({value: value})})
          .then(data => data.json()).then(resp => runs = resp['runs']);

  $: console.log(runs)

  $: x_idx = value.keys();
  $: _ = plotlyLoaded(value);

  function plotlyLoaded() {
    if(typeof Plotly !== 'undefined') {
      plot = new Plotly.react('plotHistory', [{x: x_idx, y: value, type: 'scatter'}],
              {uirevision: 1, height: '250pt'}, {responsive: true});
      plot2 = new Plotly.react('plotHistogram', [{x: Object.keys(counts), y: Object.values(counts), type: 'bar'}],
              {uirevision: 1, height: '250pt', width: '400pt'}, {responsive: false});
    }
  }
</script>

<style>
  div.row {
    display: flex;
    flex-flow: row nowrap;
  }

  div.row #keypad {
    flex: 0 1 auto;
    align-self: center;
  }

  div.row div#plotHistory {
    flex: 1 1 400pt;
    min-width: 200pt;
    width: 100%;
    height: 100%;
  }

  #runsTest {
    height: 80pt;
    line-height: 80pt;
    text-align: center;
  }

  #runsTest span {
    vertical-align: middle;
    line-height: normal;
  }
</style>

<div class="row">
  <div id="keypad">
    <Keypad bind:value bind:counts />
    <div id="runsTest"><span>{runs}</span></div>
  </div>
  <div id="plotHistory"><!-- Plotly chart will be drawn inside this DIV --></div>
  <div id="plotHistogram"><!-- Plotly chart will be drawn inside this DIV --></div>
</div>