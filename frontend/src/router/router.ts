import {createWebHistory, createRouter, type Router, type RouteRecordRaw} from "vue-router";
import APP from '../App.vue'
import AppLayout from "@/view/AppLayout.vue";
import ChatWelcome from "@/view/ChatWelcome.vue";
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
    }
]
const router: Router = createRouter({
    history: createWebHistory(),
    routes
})
export default router