<template>
	<div :class="mergedUi.wrapper">
		<slot />
	</div>
</template>
<script setup>
const ui = {
  wrapper: 'p-0 flex-1 flex flex-col overflow-y-auto'
}

const props = defineProps({
	ui: {
		type: Object,
		default: () => ({})
	}
})

defineOptions({
	inheritAttrs: false
})

const mergedUi = {
	...ui,
	...props.ui
}
</script>
