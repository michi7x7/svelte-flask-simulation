<script>
	// import { createEventDispatcher } from 'svelte';
	// const dispatch = createEventDispatcher();

	export let value = [];
	export let counts = {};

	$: counts = get_counts(value);
	// $: console.log(counts)

	function get_counts(array) {
	    let ret = {};
	    array.forEach(x => {
	        ret[x] = ret[x] + 1 || 1;
        })
        return ret;
    }

	const select = num => { value = [...value, num] };
	const clear  = () => { value = [] };
	const add_random = () => select(Math.floor(Math.random() * 10))
</script>

<style>
	.keypad {
		display: grid;
		grid-template-columns: repeat(3, 5em);
		grid-template-rows: repeat(4, 3em);
		grid-gap: 0.5em
	}

	button {
		margin: 0
	}
</style>

<div class="keypad">
	<button on:click={() => select(1)}>1</button>
	<button on:click={() => select(2)}>2</button>
	<button on:click={() => select(3)}>3</button>
	<button on:click={() => select(4)}>4</button>
	<button on:click={() => select(5)}>5</button>
	<button on:click={() => select(6)}>6</button>
	<button on:click={() => select(7)}>7</button>
	<button on:click={() => select(8)}>8</button>
	<button on:click={() => select(9)}>9</button>

	<button disabled={!value} on:click={clear}>clear</button>
	<button on:click={() => select(0)}>0</button>
	<button on:click={add_random}>random</button>
</div>
