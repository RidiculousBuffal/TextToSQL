import {defineStore} from "pinia";
import {ref} from 'vue'
import type DBConnector from "@/typeutils/DBConnector";

export const DBToken = defineStore("DBToken", () => {
    const DBToken = ref<DBConnector|undefined>(undefined)
    const setDBToken = (newDBToken: DBConnector) => {
        DBToken.value = newDBToken
    }
    const removeDBToken = ()=>{
        DBToken.value = undefined
    }
    return {DBToken,setDBToken,removeDBToken}
},{
      persist: {
        enabled: true, // 确保持久化启用
        strategies: [
            {
                key: 'DBToken', // 存储在 localStorage 中的 key
                storage: sessionStorage, // 或者 sessionStorage 视需求而定
            }
        ]
    }
})