export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxt/ui', 'nuxt-monaco-editor'],
  monacoEditor: {
      locale: 'en',
      componentName: {
          codeEditor: 'MonacoEditor'
      }
  },
  css: [
      '@/assets/styles/layout.scss'
  ]
})
