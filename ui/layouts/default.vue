<template>
	<div class="fixed inset-0 flex overflow-hidden">
		<LayoutPanel :width="250" collapsible :resizable="{ min: 200, max: 350 }">
			<LayoutNavbar title="PDF Extractor" />
			<LayoutSidebar>
				<template #header>
					<LayoutSearchButton />
				</template>
				<LayoutSidebarLink :links="routes" />
				<div class="flex-1" />
				<UDivider class="sticky bottom-0" />
				<template #footer>
					<UserDropdown />
				</template>
			</LayoutSidebar>
		</LayoutPanel>
		<slot />
	</div>
</template>
<script setup>
import LayoutPanel from "~/components/layout/LayoutPanel.vue";
import LayoutNavbar from "~/components/layout/LayoutNavbar.vue";
import LayoutSidebar from "~/components/layout/LayoutSidebar.vue";
import LayoutSearchButton from "~/components/layout/LayoutSearchButton.vue";
import UserDropdown from "~/components/common/UserDropdown.vue";
import LayoutSidebarLink from "~/components/layout/LayoutSidebarLink.vue";

const routes = [
	{
		id: 'home',
		label: 'Home',
		icon: 'i-heroicons-home',
		to: '/',
		tooltip: {
			text: 'Home'
		}
	},
	{
		id: 'extractors',
		label: 'Extractors',
		icon: 'i-heroicons-inbox',
		to: '/extractors',
		tooltip: {
			text: 'Extractors'
		}
	}
]
</script>