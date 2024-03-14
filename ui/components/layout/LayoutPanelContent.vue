<template>
	<div :class="mergedUi.wrapper">
		<slot />
	</div>
</template>
<script setup>
import {twJoin, twMerge} from "tailwind-merge";

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

const mergedUi = reactive({
	wrapper: twMerge(ui.wrapper, props.ui.wrapper)
})
</script>
