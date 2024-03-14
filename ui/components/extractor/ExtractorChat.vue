<template>
	<UForm :state="formState" :validate="validate" :validate-on="['submit']" @submit="onSubmit">
		<UTextarea color="gray" required size="xl" :rows="10" :placeholder="`Typing content here...`">
			<UInput type="file" color="gray" class="absolute bottom-2.5 left-3.5" :placeholder="`Select a file...`" />
			<UButton type="submit" color="black" label="Send" icon="i-heroicons-paper-airplane" class="absolute bottom-2.5 right-3.5" />
		</UTextarea>
	</UForm>
</template>
<script setup lang="ts">
const props = defineProps({
	extractor: {
		type: Object,
		default: undefined
	}
})

const formState = reactive({
	extractor_uuid: props.extractor?.uuid || '',
	text: '',
	file: null
})

const onSubmit = async (event) => {
	console.log(event.data)
}

const validate = (value) => {
	const errors = [];
	if (!value.text && !value.file) errors.push({ path: 'text', message: 'Text or file is required'});
	return errors;
}

</script>