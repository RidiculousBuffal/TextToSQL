import {createRouter, createWebHistory, type Router, type RouteRecordRaw} from "vue-router";
import APP from '../App.vue'
import AppLayout from "@/view/AppLayout.vue";
import ChatWelcome from "@/view/ChatWelcome.vue";
import DifyPlayground from "@/ThirdParty/DifyPlayground.vue";

const routes: Readonly<RouteRecordRaw[]> = [
    {
        path: '/',
        component: APP,
        redirect: '/welcome'
    }, {
        path: '/welcome',
        component: ChatWelcome
    }, {
        path: '/chat',
        component: AppLayout
    }, {
        path: '/dify',
        component: DifyPlayground
    }
]
const router: Router = createRouter({
    history: createWebHistory(),
    routes
})
export default router