<template>
	<ul :class="ui.wrapper">
		<li v-for="(link, index) in links"
			:key="index"
			:class="ui.container"
		>
			<div>
				<UTooltip
					v-bind="link.tooltip"
					class="flex"
					:popper="{ placement: 'right' }"
					:prevent="!link.tooltip"
					:ui="ui.tooltip"
				>
					<ULink
						v-slot="{ isActive}"
						v-bind="link.children?.length && link.collapsible !== false ? { disabled: link.disabled } : getULinkProps(link)"
						:class="[ui.base]"
						draggable="false"
						:active-class="ui.active"
						:inactive-class="(!link.to && link.collapsible === false && level === 0 && link.children?.length) ? ui.static : ui.inactive"
						@click="link.click"
					>
						<slot name="icon" :link="link" :is-active="isActive">
							<UIcon v-if="link.icon"
							       :name="link.icon"
							       :class="twMerge(
									   twJoin(
										   ui.icon.base, isActive
										   ? ui.icon.active
										   : (!link.to && link.collapsible === false && level === 0 && link.children?.length)
										        ? ui.static : ui.icon.inactive
									   ), link.iconClass)"
							/>
						</slot>
						
						<slot :link="link" :is-active="isActive">
							<span v-if="link.label" :class="twMerge(ui.label, link.labelClass)">{{ link.label }}</span>
						</slot>
					</ULink>
				</UTooltip>
			</div>
		</li>
	</ul>
</template>
<script setup lang="ts">
import type {SidebarLink} from "~/types";
import {getULinkProps} from "#ui/utils";
import {twJoin, twMerge} from "tailwind-merge";

const ui = computed(() => ({
	wrapper: 'relative !min-h-[auto] !min-w-[auto]',
	container: '!overflow-visible',
	base: 'group relative flex items-center gap-1.5 px-2.5 py-1.5 w-full rounded-md font-medium text-sm focus:outline-none focus-visible:outline-none dark:focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2 focus-visible:before:ring-primary-500 dark:focus-visible:before:ring-primary-400 before:absolute before:inset-px before:rounded-md disabled:cursor-not-allowed disabled:opacity-75',
	active: 'text-gray-900 dark:text-white before:bg-gray-100 dark:before:bg-gray-800',
	inactive: 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white hover:before:bg-gray-50 dark:hover:before:bg-gray-800/50',
    static: 'text-gray-900 dark:text-white cursor-auto',
	tooltip: {
		strategy: 'override',
		transition: {
			enterActiveClass: 'transition ease-out duration-200',
			enterFromClass: 'opacity-0',
			enterToClass: 'opacity-100',
			leaveActiveClass: 'transition ease-in duration-150',
			leaveFromClass: 'opacity-100',
			leaveToClass: 'opacity-0'
	    }
	},
	icon: {
	    base: 'flex-shrink-0 w-5 h-5 relative',
	    active: 'text-gray-900 dark:text-white',
	    inactive: 'text-gray-400 dark:text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-200'
	},
	label: 'text-sm truncate relative',
}))

defineOptions({
	inheritAttrs: false
})

const props = defineProps({
	links: {
		type: Array as PropType<SidebarLink[]>,
		default: () => []
	},
	level: {
		type: Number,
		default: 0
	}
})
</script>