<template>
	<UForm class="space-y-4"
	       :state="formState"
	       :validate="validate"
	       :validate-on="['submit']"
	       @submit="onSubmit">
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
			              :options="{automaticLayout: true, minimap: { enabled: false }, theme: 'vs-dark'}"
			              lang="json"
			/>
		</UFormGroup>
		<div class="flex justify-end gap-3">
			<UButton @click="() => $emit('close')" color="gray" variant="ghost" label="Cancel" />
			<UButton type="submit" label="Save" color="black" />
		</div>
	</UForm>
</template>
<script setup>
const emit = defineEmits(['close']);

const schemaDefault = `{
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
}`
const props = defineProps({
	extractor: {
		type: Object,
		default: undefined
	}
})

const formState = reactive({
	name: props.extractor?.name || '',
	description: props.extractor?.description || '',
	prompt: props.extractor?.prompt || '',
	schema: props.extractor?.schema || schemaDefault
})
const validate = (value) => {
	const errors = [];
	if (!value.name) errors.push({ path: 'name', message: 'Name is required'});
	if (!value.description) errors.push({ path: 'description', message: 'Description is required'});
	if (!value.prompt) errors.push({ path: 'prompt', message: 'Prompt is required'});
	if (!value.schema) errors.push({ path: 'schema', message: 'Schema is required'});
	
	try {
		JSON.parse(value.schema);
	} catch (e) {
		errors.push({ path: 'schema', message: 'Schema is not a valid JSON'});
	}
	
	return errors;
}

async function onSubmit(event) {
	console.log(event.data)
	emit('close')
}
</script>
<style>
.monaco-editor {
	height: 15rem!important;
}
</style>