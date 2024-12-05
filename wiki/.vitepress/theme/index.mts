import DefaultTheme from 'vitepress/theme-without-fonts'
import MyLayout from './layout/transitions.vue'

import type { Theme } from 'vitepress'

import { enhanceAppWithTabs } from 'vitepress-plugin-tabs/client'

import './style/index.css'

export default {
    extends: DefaultTheme,

    Layout: MyLayout,

    enhanceApp({ app }) {
        enhanceAppWithTabs(app)
    },
} satisfies Theme