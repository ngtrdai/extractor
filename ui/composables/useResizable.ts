import {useCookie} from "#app";

export const useResizable = (
    key: string,
    { min, max, value = 0 }: { min?: number, max?: number, value?: number }
) => {
    const el =  ref<HTMLElement | null>(null);
    const width = useCookie<number>(key, { default: () => value});
    const isResizing = ref(false);

    const onMouseMove = (e: MouseEvent, x: number) => {
        let w = el.value!.offsetWidth + e.clientX - x;

        if (min) {
            w = Math.max(w, min);
        }

        if (max) {
            w = Math.min(w, max);
        }

        width.value = w;

        return e.clientX;
    }

    const onDrag = (e: MouseEvent) => {
        if (!el.value) return;

        let x = e.clientX;

        document.onmousemove = (e) => {
            isResizing.value = true;
            x = onMouseMove(e, x);
        }

        document.onmouseup = () => {
            document.onmousemove = null;
            document.onmouseup = null;
            isResizing.value = false;
        }
    }

    return {
        el,
        width,
        isResizing,
        onDrag
    }
}