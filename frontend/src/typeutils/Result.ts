export default interface Result<T>{
    status:string,
    message?:T,
    payload?:any
}
