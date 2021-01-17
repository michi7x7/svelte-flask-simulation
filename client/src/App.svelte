<svelte:head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>


<script>
  export let plotHeader = 'Server Load History';
  
  function doUpdate(response) {
    Plotly.react('plotDiv', [{x: response.time, y: response.load, type: 'scatter'}], {uirevision:'true'});
  }

  function updatePlot() {
    fetch("./get_load").then(d => d.json()).then(doUpdate);
  }

  setInterval(updatePlot, 1000);
</script>

<div id="plotly">
  <div>
    <h1>{plotHeader}</h1>
  </div>
  <div id="plotDiv"><!-- Plotly chart will be drawn inside this DIV --></div>
</div>
