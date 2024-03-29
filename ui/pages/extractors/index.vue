<template>
	<LayoutPage>
		<LayoutPanel id="extractors" :width="300" :resizable="{ min: 250, max: 350 }">
			<LayoutNavbar title="Extractors">
				<template #right>
					<UButton trailing-icon="i-heroicons-plus" @click="isShowCreateModal = true">New</UButton>
				</template>
			</LayoutNavbar>
			<ExtractorList v-model="selected" :extractors="extractors" v-if="isLoaded" />
			<template v-else>
				<div class="flex items-center space-x-4 p-4">
					<div class="space-y-2">
						<USkeleton class="h-4 w-[200px]" />
						<USkeleton class="h-4 w-[150px]" />
					</div>
				</div>
			</template>
			<BaseModal v-model="isShowCreateModal"
			           title="New Extractor"
			           description="Create a new extractor"
			>
				<ExtractorForm @close="isShowCreateModal = false" @submitted="handleFormSubmitted" />
			</BaseModal>
		</LayoutPanel>
		<LayoutPanel collapsible grow side="right" v-model="isDetailPanelOpen">
			<template v-if="selected">
				<LayoutNavbar>
					<template #left>
						<UTooltip text="Edit Extractor">
							<UButton icon="i-heroicons-command-line"
							         color="gray"
							         variant="ghost"
							         @click="isShowEditSchemaModal = true" />
						</UTooltip>
						<BaseModal v-model="isShowEditSchemaModal"
						           title="Edit Extractor"
						           description="Edit the extractor"
	
						>
							<ExtractorForm :extractor="selected" @close="isShowEditSchemaModal = false" @submitted="handleFormSubmitted" />
						</BaseModal>
					</template>
					<template #right>
						<UDropdown :items="detailItems">
							<UButton icon="i-heroicons-ellipsis-vertical" color="gray" variant="ghost" />
						</UDropdown>
					</template>
				</LayoutNavbar>
				<ExtractorDetail :extractor="selected" />
			</template>
			<div v-else class="flex-1 hidden lg:flex items-center justify-center">
				<UIcon name="i-heroicons-cube-transparent" class="w-32 h-32 text-gray-400 dark:text-gray-500" />
			</div>
		</LayoutPanel>
	</LayoutPage>
</template>
<script setup>
import BaseModal from "~/components/common/BaseModal.vue";
import ExtractorService from "~/services/ExtractorService.ts";

const isLoaded = ref(false);
const isShowCreateModal = ref(false);
const isShowEditSchemaModal = ref(false);
const selected = ref();
const extractors = ref([]);
const toast = useToast();

onMounted(async () => {
	extractors.value = await new ExtractorService().getExtractors();
	isLoaded.value = true;
})

const detailItems = [
	[
		{
			label: 'Delete',
			icon: 'i-heroicons-trash',
			click: () => {
				toast.add({
					title: 'Delete Extractor',
					description: 'Are you sure you want to delete this extractor?',
					color: "red",
					icon: 'i-heroicons-trash',
					actions: [
						{
							label: 'Delete',
							variant: 'solid',
							color: 'red',
							onClick: () => {
								toast.remove();
								onDeleteExtractor();
							}
						}, {
							label: 'Cancel',
							variant: 'ghost',
							onClick: () => toast.remove()
						}
					]
				})
			}
		}
	]
]

const isDetailPanelOpen = computed({
	get: () => !!selected.value,
	set: (value) => {
		if (!value) selected.value = null;
	}
})

const handleFormSubmitted = async () => {
	isLoaded.value = false;
	extractors.value = await new ExtractorService().getExtractors();
	isLoaded.value = true;
}

const onDeleteExtractor = async () => {
	isLoaded.value = false;
	await new ExtractorService().deleteExtractor(selected.value.uuid).then(() => {
		toast.add({
			title: 'Extractor Deleted',
			description: 'The extractor has been deleted',
			color: 'green',
			icon: 'i-heroicons-check'
		})
		selected.value = null;
	}).catch(() => {
		toast.add({
			title: 'Error',
			description: 'An error occurred while deleting the extractor',
			color: 'red',
			icon: 'i-heroicons-x'
		})
	}).finally(async () => {
		extractors.value = await new ExtractorService().getExtractors();
		isLoaded.value = true;
	})
}
</script>