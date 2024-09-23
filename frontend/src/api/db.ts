import ins from '@/request/request'
import type DBConnector from "../typeutils/DBConnector";
import type Result from "@/typeutils/Result";

export const checkDBConnection = async (payload: DBConnector): Promise<Result> => {
    try {
        return await ins.post('/checkDB', payload); // 返回响应数据
    } catch (error) {
        console.error('Error checking DB connection:', error);
        throw error;
    }
}
export const uploadFile = async (payload: FormData): Promise<Result> => {
    try {
        console.log(payload)
        return await ins.post('/uploadTable', payload, {
            headers: {
                'Content-Type': 'multipart/form-data' // 确保设置正确的 Content-Type
            }
        });

    } catch (error) {
        // 处理错误
        console.error('上传文件时出错:', error);
        throw error; // 可以选择抛出错误或返回自定义错误对象
    }
}