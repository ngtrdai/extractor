export default defineAppConfig({
    ui: {
        variables: {
            header: {
                height: '4rem'
            },
            light: {
                background: '255 255 255',
                foreground: 'var(--color-gray-700)'
            },
            dark: {
                background: 'var(--color-gray-900)',
                foreground: 'var(--color-gray-200)'
            }
        },
        icons: {
            search: 'i-heroicons-magnifying-glass-20-solid'
        },
        themes: {
            button: {
                primary: {
                    color: 'white',
                    variant: 'solid'
                },
                secondary: {
                    color: 'gray',
                    variant: 'solid'
                }
            }
        }
    }
});