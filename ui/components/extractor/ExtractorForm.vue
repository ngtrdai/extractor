<template>
	<UForm class="space-y-4">
		<UFormGroup label="Name" name="name" required>
			<UInput v-model="formState.name" placeholder="My CV" />
		</UFormGroup>
		<UFormGroup label="Description" name="description" required>
			<UInput v-model="formState.description" placeholder="My CV Extractor" />
		</UFormGroup>
		<UFormGroup label="Prompt" name="prompt" required>
			<UTextarea  v-model="formState.prompt" placeholder="Use information from your CV to fill in the form" />
		</UFormGroup>
		<UFormGroup label="Schema" name="schema" required>
			<MonacoEditor v-model="formState.schema"
			              lang="json"
			              
			/>
		</UFormGroup>
	</UForm>
</template>
<script setup>
const formState = reactive({
	name: '',
	description: '',
	prompt: '',
	schema: ''
})
</script>