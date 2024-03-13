<template>
	<UDropdown
		mode="hover"
		:items="items"
		class="w-full"
		:ui="{ width: 'w-full', item: { disabled: 'cursor-text select-text' } }"
		:popper="{ strategy: 'absolute', placement: 'top' }"
	>
		<template #default="{ open }">
			<UButton
				v-bind="appConfig.ui.themes.button.secondary"
				variant="ghost"
				class="w-full"
				label="Dai Nguyen Trong"
				:class="[open ? 'bg-gray-50 dark:bg-gray-800' : '']"
			>
				<template #leading>
					<UAvatar src="https://avatars.githubusercontent.com/u/739984?v=4" size="2xs" />
		        </template>
				
				<template #trailing>
					<UIcon name="i-heroicons-ellipsis-vertical" class="w-5 h-5 ml-auto" />
				</template>
			</UButton>
		</template>
		
		<template #account>
			<div class="text-left">
				<p>Signed in as</p>
				<p class="truncate font-medium text-gray-900 dark:text-white">ngtrdai@hotmail.com</p>
			</div>
		</template>
	</UDropdown>
</template>
<script setup>
const appConfig = useAppConfig();
const { metaSymbol } = useShortcuts();

const items = computed(() => [
	[{
	    slot: 'account',
	    label: '',
	    disabled: true
    }],
	[{
		label: 'Sign out',
	    icon: 'i-heroicons-arrow-left-on-rectangle'
	}]
]);
</script>