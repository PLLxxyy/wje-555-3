import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import permission from './directives/permission'
import './styles/index.scss'

createApp(App).use(createPinia()).use(router).use(ElementPlus).use(permission).mount('#app')

