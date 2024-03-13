<template>
	<div
		ref="el"
		:class="[ui.wrapper, grow ? ui.grow : ui.border, collapsible ? 'hidden lg:flex' : 'flex']"
		:style="{ '--width': width && !grow ? `${width}px` : undefined }"
	>
		<slot />
		
		<slot name="handle">
			<div :class="ui.handle.wrapper" v-if="resizable" @mousedown="onDrag">
				<div :class="ui.handle.container" />
			</div>
		</slot>
	</div>
</template>
<script setup>
const ui = {
	wrapper: 'flex-col items-stretch relative w-full',
	border: 'border-b lg:border-b-0 lg:border-r border-gray-200 dark:border-gray-800 lg:w-[--width] flex-shrink-0',
	grow: 'flex-1',
	handle: {
		wrapper: 'hidden md:block bg-transparent select-none absolute z-50 group w-[9px] h-full inset-y-0 -right-[5px] cursor-col-resize',
		container: 'group-hover:bg-gray-300 dark:group-hover:bg-gray-700 transition duration-200 absolute w-px h-full inset-x-0 mx-auto'
	}
}

const props = defineProps({
	id: {
		type: String,
		default: undefined
	},
	modelValue: {
		type: Boolean,
		default: false
	},
	width: {
		type: Number,
		default: undefined
	},
	grow: {
		type: Boolean,
		default: false
	},
	collapsible: {
		type: Boolean,
		default: false
	},
	resizable: {
		type: [Boolean, Object],
		default: false
	},
	className: {
		type: String,
		default: undefined
	}
})

const emit = defineEmits(['update:modelValue']);
const id = props.id ? `layout:panel:${props.id}` : useId(`layout:panel`);
const { el, width, onDrag, isResizing } = props.resizable
	? useResizable(
		id,
		{
			...(
				typeof props.resizable === 'object'
				? props.resizable
				: {}
			),
			value: props.width
		})
	: { el: undefined, width: toRef(props.width), onDrag: undefined, isDragging: undefined }

defineExpose({
	width,
	isResizing
})
</script>