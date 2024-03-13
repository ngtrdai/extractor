<template>
	<div :class="ui.wrapper">
		<slot />
	</div>
</template>
<script setup>
const ui = {
  wrapper: 'p-0 flex-1 flex flex-col overflow-y-auto'
}
</script>
