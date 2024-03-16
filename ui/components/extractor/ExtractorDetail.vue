<template>
	<LayoutPanelContent :ui="{wrapper: 'p-4'}">
		<div class="flex justify-between">
			<div class="flex items-center gap-4">
				<div class="min-w-0">
					<h1 class="text-2xl font-semibold text-gray-900 dark:text-white truncate">
						{{ extractor.name }}
					</h1>
					<p class="mt-1 text-sm text-gray-500 dark:text-gray-400">
						{{ extractor.description }}
					</p>
				</div>
			</div>
			<p class="font-medium text-gray-900 dark:text-white">
				{{ isToday(new Date(extractor.created_at)) ? format(new Date(extractor.created_at), 'HH:mm') : format(new Date(extractor.created_at), 'dd MMM') }}
			</p>
		</div>
		<UDivider class="my-5" />
		<div class="flex flex-1">
			<p class="text-lg">
				{{ extractedData }}
			</p>
		</div>
		<UDivider class="my-5" />
		<ExtractorChat :extractor="extractor" v-model="extractedData" @update:modelValue="handleExtractedData" />
	</LayoutPanelContent>
</template>
<script setup lang="ts">
import type { Extractor } from '~/types';
import {format, isToday} from "date-fns";
const props = defineProps({
	extractor: {
		type: Object as PropType<Extractor>,
		default: undefined
	}
})

const extractedData = ref(null)

const handleExtractedData = (data) => {
	console.log(data)
}
</script>