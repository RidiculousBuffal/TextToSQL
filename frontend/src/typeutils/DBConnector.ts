export default interface DBConnector {
    DB_URL: string;
    DB_USERNAME: string;
    DB_PASSWORD: string;
    DB_PORT:string;
    DB_NAME?: string; // 可选属性
}
