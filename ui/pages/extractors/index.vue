<template>
	<LayoutPage>
		<LayoutPanel id="extractors" :width="300" :resizable="{ min: 250, max: 350 }">
			<LayoutNavbar title="Extractors">
				<template #right>
					<UButton trailing-icon="i-heroicons-plus" @click="isShowCreateModal = true">New</UButton>
				</template>
			</LayoutNavbar>
			<ExtractorList v-model="selected" :extractors="extractors" />
			<BaseModal v-model="isShowCreateModal"
			           title="New Extractor"
			           description="Create a new extractor"
			>
				<ExtractorForm @close="isShowCreateModal = false" />
			</BaseModal>
		</LayoutPanel>
		<LayoutPanel collapsible grow side="right" v-model="isDetailPanelOpen">
			<template v-if="selected">
				<LayoutNavbar>
					<template #left>
						<UTooltip text="Edit Schema">
							<UButton icon="i-heroicons-command-line"
							         color="gray"
							         variant="ghost"
							         @click="isShowEditSchemaModal = true" />
						</UTooltip>
						<BaseModal v-model="isShowEditSchemaModal"
						           title="Edit Schema"
						           description="Edit the schema of the extractor"
						>
							<ExtractorForm :extractor="selected" @close="isShowEditSchemaModal = false" />
						</BaseModal>
					</template>
					<template #right>
						<UDropdown :items="detailItems">
							<UButton icon="i-heroicons-ellipsis-vertical" color="gray" variant="ghost" />
						</UDropdown>
					</template>
				</LayoutNavbar>
				<ExtractorDetail :extractor="selected" :ui="{wrapper: 'p-4'}" />
			</template>
			<div v-else class="flex-1 hidden lg:flex items-center justify-center">
				<UIcon name="i-heroicons-cube-transparent" class="w-32 h-32 text-gray-400 dark:text-gray-500" />
			</div>
		</LayoutPanel>
	</LayoutPage>
</template>
<script setup>
import BaseModal from "~/components/common/BaseModal.vue";

const isShowCreateModal = ref(false);
const isShowEditSchemaModal = ref(false);
const selected = ref();
const extractors = [
	{
		uuid: '1',
		name: 'Extractor 1',
		description: 'This is the first extractor',
		prompt: 'This is the first extractor',
		schema: `{
			"type": "object",
			"properties": {
				"firstName": {
					"type": "string",
					"description": "The person's first name."
				},
				"lastName": {
					"type": "string",
					"description": "The person's last name."
				},
				"age": {
					"description": "Age in years which must be equal to or greater than zero.",
					"type": "integer",
					"minimum": 0
				}
			}
		}`,
		created_at: '2021-10-01T00:00:00Z'
	},
	{
		uuid: '2',
		name: 'Extractor 2',
		description: 'This is the second extractor',
		prompt: 'This is the second extractor',
		schema: `{
			"type": "object",
			"properties": {
				"firstName": {
					"type": "string",
					"description": "The person's first name."
				},
				"lastName": {
					"type": "string",
					"description": "The person's last name."
				},
				"age": {
					"description": "Age in years which must be equal to or greater than zero.",
					"type": "integer",
					"minimum": 0
				}
			}
		}`,
		created_at: '2021-10-02T00:00:00Z'
	}
];

const detailItems = [
	[
		{
			label: 'Delete',
			icon: 'i-heroicons-trash',
		}
	]
]

const isDetailPanelOpen = computed({
	get: () => !!selected.value,
	set: (value) => {
		if (!value) selected.value = null;
	}
})
</script>