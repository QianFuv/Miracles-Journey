import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme-without-fonts'
import { enhanceAppWithTabs } from 'vitepress-plugin-tabs/client'

import './style/index.css'

import MyLayout from './layout/transitions.vue'

import mediumZoom from 'medium-zoom';
import { onMounted, watch, nextTick } from 'vue';
import { useRoute } from 'vitepress';

export default {
    extends: DefaultTheme,
    Layout: MyLayout,
    setup() {
        const route = useRoute();
        const initZoom = () => {
            // mediumZoom('[data-zoomable]', { background: 'var(--vp-c-bg)' }); // 默认
            mediumZoom('.main img', { background: 'var(--vp-c-bg)' }); // 不显式添加{data-zoomable}的情况下为所有图像启用此功能
        };
        onMounted(() => {
            initZoom();
        });
        watch(
            () => route.path,
            () => nextTick(() => initZoom())
        );
    },
    enhanceApp({ app }) {
        enhanceAppWithTabs(app)
    },
} satisfies Theme