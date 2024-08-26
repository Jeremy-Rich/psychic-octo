<<<<<<< HEAD
module.exports = [
  {
    files: ['**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      parser: require('@typescript-eslint/parser'),
      globals: {
        fetch: 'readonly',
        console: 'readonly',
        self: 'readonly',
        window: 'readonly',
        document: 'readonly',
        navigator: 'readonly',
        HTMLElement: 'readonly',
        Node: 'readonly',
        MutationObserver: 'readonly',
        KeyframeEffect: 'readonly',
        CSS: 'readonly',
        Blob: 'readonly',
        FileReader: 'readonly',
        Image: 'readonly',
        XMLHttpRequest: 'readonly',
        FormData: 'readonly',
        setTimeout: 'readonly',
        setInterval: 'readonly',
        clearTimeout: 'readonly',
        clearInterval: 'readonly',
        requestAnimationFrame: 'readonly',
        cancelAnimationFrame: 'readonly',
        OffscreenCanvas: 'readonly',
        ImageBitmap: 'readonly',
        TextEncoder: 'readonly',
        TextDecoder: 'readonly',
        WebGLRenderingContext: 'readonly',
        WebGL2RenderingContext: 'readonly',
        WebGLComputeRenderingContext: 'readonly',
        XRWebGLLayer: 'readonly',
        XRWebGLBinding: 'readonly',
        __THREE_DEVTOOLS__: 'readonly',
        CustomEvent: 'readonly',
        createImageBitmap: 'readonly',
        Headers: 'readonly',
        Request: 'readonly',
        Response: 'readonly',
        DOMParser: 'readonly',
        ReadableStream: 'readonly',
        ProgressEvent: 'readonly',
        performance: 'readonly',
        process: 'readonly',
        global: 'readonly',
        atob: 'readonly',
        btoa: 'readonly',
        Buffer: 'readonly',
        ImageData: 'readonly',
        HTMLCanvasElement: 'readonly',
        HTMLImageElement: 'readonly',
        HTMLVideoElement: 'readonly',
        ga: 'readonly',
        alert: 'readonly',
        SECRET: 'readonly',
        EVALEX_TRUSTED: 'readonly',
        CONSOLE_MODE: 'readonly',
        EVALEX: 'readonly',
        parent: 'readonly',
        navigate: 'readonly',
        select: 'readonly',
        location: 'readonly',
        group: 'readonly',
        XMLHTTPRequest: 'readonly',
      },
    },
  },
];
=======
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
)
>>>>>>> 6d322ea (Initial commit)
