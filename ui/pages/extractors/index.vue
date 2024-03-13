<template>
	<LayoutPage>
		<LayoutPanel :width="300" :resizable="{ min: 250, max: 350 }">
			<LayoutNavbar title="Extractors">
				<template #right>
					<UButton to="/extractors/create">
						New Extractor
					</UButton>
				</template>
			</LayoutNavbar>
		</LayoutPanel>
	</LayoutPage>
</template>
<script setup>
</script>