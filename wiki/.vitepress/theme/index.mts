import DefaultTheme from 'vitepress/theme-without-fonts'
import type { Theme } from 'vitepress'

import { enhanceAppWithTabs } from 'vitepress-plugin-tabs/client'

import './style/index.css'

export default {
    extends: DefaultTheme,

    enhanceApp({ app }) {
        enhanceAppWithTabs(app)
    },
} satisfies Theme