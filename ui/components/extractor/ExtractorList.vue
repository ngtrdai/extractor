<template>
	<LayoutPanelContent>
		<div v-for="(extractor, index) in extractors" :key="index" :ref="el => extractorsRefs[extractor.uuid] = el as Element">
			<div :class="[
					ui.container,
					selected && selected.uuid === extractor.uuid ? ui.selected : ui.unselected
				]"
			     @click="selected = extractor"
			>
				<div class="flex items-center justify-between">
					<div class="flex items-center gap-3 font-semibold">
						{{ extractor.name }}
					</div>
					<span>
						{{
							isToday(new Date(extractor.created_at))
							? format(new Date(extractor.created_at), 'HH:mm')
							: format(new Date(extractor.created_at), 'dd MMM')
						}}
					</span>
				</div>
				<p class="text-gray-400 dark:text-gray-500 line-clamp-1">
					{{ extractor.description }}
		        </p>
			</div>
		</div>
	</LayoutPanelContent>
</template>
<script setup lang="ts">
import type {PropType} from "vue";
import type {Extractor} from "~/types";
import { format, isToday } from 'date-fns'

const ui = {
	container: 'p-4 text-sm cursor-pointer border-l-2 text-gray-900 dark:text-white',
	selected: 'border-primary-500 dark:border-primary-400 bg-primary-100 dark:bg-primary-900/25',
	unselected: 'border-white dark:border-gray-900 hover:border-primary-500/25 dark:hover:border-primary-400/25 hover:bg-primary-100/50 dark:hover:bg-primary-900/10'
}

const props = defineProps({
	modelValue: {
		type: Object as PropType<Extractor | null>,
		default: null
	},
	extractors: {
		type: Array as PropType<Extractor[]>,
		default: () => []
	}
})

const emit = defineEmits(['update:modelValue'])
const extractorsRefs = ref<Element[]>([])
const selected = computed({
	get: () => props.modelValue,
	set: (value) => emit('update:modelValue', value)
})

watch(selected, () => {
	if (!selected.value) return
	
	const ref = extractorsRefs.value[selected.value.uuid]
	if (ref) {
		ref.scrollIntoView({ block: 'nearest' })
	}
});
</script>