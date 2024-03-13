<template>
	<UModal v-model="isOpen" prevent-close>
		<div :class="[ui.header.base, ui.header.padding]">
			<slot name="header">
				<div :class="ui.header.inner">
					<div>
						<p v-if="title || $slots.title" :class="ui.title">
							<slot name="title">
								{{ title }}
							</slot>
			            </p>
			
			            <p v-if="description || $slots.description" :class="ui.description">
				            <slot name="description">
					            {{ description }}
				            </slot>
			            </p>
					</div>
				</div>
				<UButton v-if="closeButton"
				         aria-label="Close"
				         v-bind="{...ui.closeButton, ...closeButton}"
				         @click="isOpen = false" />
			</slot>
		</div>
		<div v-if="$slots.default" :class="[ui.body.base, ui.body.padding]">
			<slot />
		</div>
		<div v-if="$slots.footer" :class="[ui.footer.base, ui.footer.padding]">
			<slot name="footer" />
		</div>
	</UModal>
</template>
<script setup>
import {twMerge} from "tailwind-merge";
const slots = useSlots();
const appConfig = useAppConfig();
const ui = {
	title: 'text-gray-900 dark:text-white font-semibold',
	description: 'mt-1 text-gray-500 dark:text-gray-400 text-sm',
	header: {
		base: 'flex items-start justify-between gap-x-1.5 flex-shrink-0 min-h-[--header-height]',
		inner: 'flex items-start gap-4',
		padding: twMerge('px-4 py-4 sm:px-6', (slots.default || slots.footer) ? 'pb-0' : undefined)
	},
	body: {
		base: 'flex-1 flex flex-col gap-y-3 overflow-y-auto',
		padding: 'px-4 py-5 sm:p-6'
	},
	footer: {
		base: 'flex items-center gap-x-1.5 flex-shrink-0',
		padding: 'px-4 py-4 sm:px-6'
	},
	closeButton: {
		icon: appConfig.ui.icons.close,
		color: 'gray',
		variant: 'ghost',
		size: 'sm'
    }
}

defineOptions({
  inheritAttrs: false
})

const props = defineProps({
	modelValue: {
		type: Boolean,
		default: false
	},
	title: {
		type: String,
		default: undefined
	},
	description: {
		type: String,
		default: undefined
	},
	closeButton: {
		type: Object,
		default: () => ({})
	},
})

const emit = defineEmits(['update:modelValue'])
const isOpen = computed({
	get: () => props.modelValue,
	set: (value) => emit('update:modelValue', value)
})
</script>