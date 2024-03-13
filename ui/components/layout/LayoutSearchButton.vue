<template>
	<UButton
		:label="label"
		:icon="appConfig.ui.icons.search"
		v-bind="appConfig.ui.themes.button.secondary"
		aria-label="Search"
		truncate
		@click="toggleSearchModal"
	/>
</template>
<script setup>
import {useLayoutState} from "~/composables/useLayoutState.ts";

const appConfig = useAppConfig()
const { toggleSearchModal } = useLayoutState()

const props = defineProps({
	label: {
		type: String,
		default: 'Search...'
	}
})
</script>