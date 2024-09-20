import axios, {type AxiosInstance} from "axios";
import {ElNotification} from "element-plus";

const ins:AxiosInstance = axios.create({
    baseURL:import.meta.env.VITE_APP_BACKEND_URL
})

ins.interceptors.response.use((resp)=>{
    return resp.data
},(error)=>{
    ElNotification({
        title:"Error",
        message:"请求错误",
        type:'error'
    })
})

export default ins