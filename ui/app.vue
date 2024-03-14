<template>
	<div>
		<NuxtLoadingIndicator />
		<NuxtLayout layout="default">
			<NuxtPage />
		</NuxtLayout>
		<UModals />
		<UNotifications />
	</div>
</template>
<script setup>
useHead({
	meta: [
		{ charset: 'utf-8' },
		{ name: 'viewport', content: 'width=device-width, initial-scale=1' }
	]
})

const title = 'Extractor'
const description = 'Extract text from PDF files'
useSeoMeta({
	title,
	description,
	ogTitle: title,
	ogDescription: description
})
</script>