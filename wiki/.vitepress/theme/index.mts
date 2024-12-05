import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme-without-fonts'
import { enhanceAppWithTabs } from 'vitepress-plugin-tabs/client'

import './style/index.css'

import MyLayout from './layout/transitions.vue'

export default {
    extends: DefaultTheme,
    Layout: MyLayout,
    enhanceApp({ app }) {
        enhanceAppWithTabs(app)
    },
} satisfies Theme