import {defineStore} from "pinia";
import {ref} from 'vue'
//@ts-ignore
export const AiSearchState = defineStore('AiSearch', () => {
    const state = ref<boolean>(false)
    const setState = (newstate: boolean) => {
        state.value = newstate
    }
    return {state,setState}
}, {
    persist: {
        enabled: true, // 确保持久化启用
        strategies: [
            {
                key: 'AiSearch', // 存储在 localStorage 中的 key
                storage: sessionStorage, // 或者 sessionStorage 视需求而定
            }
        ]
    }
})