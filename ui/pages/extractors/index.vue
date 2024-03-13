<template>
	<LayoutPage>
		<LayoutPanel :width="300" :resizable="{ min: 250, max: 350 }">
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
				<ExtractorForm />
			</BaseModal>
		</LayoutPanel>
	</LayoutPage>
</template>
<script setup>
import BaseModal from "~/components/common/BaseModal.vue";

const isShowCreateModal = ref(false);
const selected = ref();
const extractors = [
	{
		uuid: '1',
		name: 'Extractor 1',
		description: 'This is the first extractor',
		created_at: '2021-10-01T00:00:00Z'
	},
	{
		uuid: '2',
		name: 'Extractor 2',
		description: 'This is the second extractor',
		created_at: '2021-10-02T00:00:00Z'
	}
]
</script>