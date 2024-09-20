import {ElNotification} from "element-plus";

export const MyNotification=(type:"success"|"error",message:string,title:string)=>{
    return ElNotification({
        type:type,
        title:title,
        message:message
    })
}