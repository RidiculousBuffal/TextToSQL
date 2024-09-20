import ins from '@/request/request'
import DBConnector from "../src/typeutils/DBConnector";
import Result from "../src/typeutils/Result";

export const checkDBConnection = async (payload:DBConnector):Promise<Result>=>{
 try {
     return await ins.post('/checkDB', payload); // 返回响应数据
    } catch (error) {
        console.error('Error checking DB connection:', error);
        throw error;
    }
}