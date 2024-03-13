<template>
	<div :class="ui.wrapper">
		<div :class="ui.container">
			<div :class="ui.left">
				<slot name="left">
					<h1 v-if="title" :class="ui.title">
						<slot name="title">
							<span class="truncate">{{ title }}</span>
						</slot>
					</h1>
				</slot>
			</div>
			<div v-if="$slots.right" :class="ui.right">
				<slot name="right" />
			</div>
		</div>
	</div>
</template>
<script setup>

const appConfig = useAppConfig();

const ui = {
	wrapper: `h-[4rem] flex-shrink-0 flex items-center border-b border-gray-200 dark:border-gray-800 px-4 gap-x-4 min-w-0`,
	container: 'flex items-center justify-between flex-1 gap-x-1.5 min-w-0',
	left: 'flex items-stretch gap-1.5 min-w-0 flex-1',
	title: 'flex items-center gap-1.5 font-semibold text-gray-900 dark:text-white min-w-0',
	right: 'flex items-stretch flex-shrink-0 gap-1.5'
}

const props = defineProps({
	title: {
		type: String,
		default: undefined
	}
})
</script>