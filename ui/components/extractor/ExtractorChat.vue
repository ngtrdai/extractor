<template>
	<UForm :state="formState"
	       :validate="validate"
	       :validate-on="['submit']"
	       @submit="onSubmit">
		<UFormGroup name="text">
			<UTextarea
				color="gray"
				size="xl"
				:rows="10"
				:placeholder="`Typing content here...`"
				name="text"
				v-model="formState.text"
			>
				
				<UFormGroup
					name="file"
					class="absolute bottom-2.5 left-3.5"
					:ui="{ container: 'flex flex-wrap items-center gap-3', help: 'mt-0' }"
				>
					<UInput
						type="file"
						color="gray"
						accept="application/pdf"
						:placeholder="`Select a file...`"
						@change="onFileChange"
					/>
		        </UFormGroup>
				<UButton type="submit" color="black" label="Send" icon="i-heroicons-paper-airplane" class="absolute bottom-2.5 right-3.5" />
			</UTextarea>
		</UFormGroup>
	</UForm>
</template>
<script setup lang="ts">
import ExtractService from "~/services/ExtractService";

const emit = defineEmits(['update:modelValue']);
const props = defineProps({
	modelValue: {
		type: String,
		default: null
	},
	extractor: {
		type: Object,
		required: true
	}
})

const isExtracting = ref(false);

const formState = reactive({
	extractor_uuid: props.extractor?.uuid || '',
	text: '',
	file: null
})

const onFileChange = (event) => {
	const file = event.target as HTMLInputElement;
	
	if (!file.files || !file.files[0]) return;
	
	formState.file = file.files[0];
}

const onSubmit = async (event) => {
	isExtracting.value = true;
	await new ExtractService().extractData(event.data).then((response) => {
		emit('update:modelValue', response.text);
	}).finally(() => {
		isExtracting.value = false;
	});
}

const validate = (value) => {
	const errors = [];
	if (!value.text && !value.file) errors.push({ path: 'text', message: 'Text or file is required'});
	return errors;
}

</script>