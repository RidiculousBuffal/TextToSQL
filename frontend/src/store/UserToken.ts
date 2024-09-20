import {defineStore} from "pinia";
import {ref} from 'vue'

export const userToken = defineStore('userToken20240913', () => {
    const token = ref<string | undefined>(undefined)
    const setToken = function (token_: string) {
        token.value = token_
    }
    const removeToken = function () {
        token.value = undefined
    }
    return {token, setToken, removeToken}
}, {
    persist: {
        enabled: true,
        strategies: [
            {
                key: 'userToken20240913', // 存储在 localStorage 中的 key
                storage: sessionStorage, // 或者 sessionStorage 视需求而定
            }
        ]
    }
})