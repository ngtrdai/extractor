<template>
	<div :class="ui.wrapper">
		<div :class="ui.container">
			<div v-if="$slots.header" :class="ui.header">
				<slot name="header" />
			</div>
			<div :class="ui.body">
				<slot />
			</div>
			<div v-if="$slots.footer" :class="ui.footer">
				<slot name="footer" />
			</div>
		</div>
	</div>
</template>
<script setup>
const ui = {
	wrapper: 'flex flex-col w-full flex-1 relative overflow-hidden',
	container: 'flex-grow flex flex-col min-h-0 gap-y-2 py-2',
	header: 'w-full flex flex-col px-4',
	body: 'flex-1 px-4 flex flex-col gap-y-2 overflow-y-auto',
	footer: 'flex items-center justify-between gap-x-1.5 flex-shrink-0 px-4'
}

defineOptions({
	inheritAttrs: false
})
</script>