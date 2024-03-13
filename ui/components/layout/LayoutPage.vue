<template>
	<div :class="ui.wrapper">
		<slot />
	</div>
</template>
<script setup>
const ui = {
	wrapper: 'flex flex-1 w-full min-w-0'
}

defineOptions({
	inheritAttrs: false
})
</script>