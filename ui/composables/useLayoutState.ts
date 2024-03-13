import {createSharedComposable} from "@vueuse/shared";

const _useLayoutState = () => {
    const isSearchModalOpen = ref(false);

    const toggleSearchModal = () => {
        isSearchModalOpen.value = !isSearchModalOpen.value;
    }

    return {
        isSearchModalOpen,
        toggleSearchModal
    }
}

export const useLayoutState = createSharedComposable(_useLayoutState)