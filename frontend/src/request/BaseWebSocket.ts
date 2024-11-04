import type {AllowedEndpoint} from "@/typeutils/availableEndPoint";
const BASE_URL = import.meta.env.VITE_APP_BACKEND_URL
export default function (endpoint:AllowedEndpoint,messageFunc:(event:MessageEvent)=>{},closeFunc:(event:CloseEvent)=>{},openFunc:(event:Event)=>{},errorFunc:(event:Event)=>{}){
    const websocket =  new WebSocket(`wss://${BASE_URL}${endpoint}`)
    websocket.addEventListener('message',messageFunc)
    websocket.addEventListener('close',closeFunc)
    websocket.addEventListener('open',openFunc)
    websocket.addEventListener('error',errorFunc)
    return websocket
}
export function sendWebSocket(ws:WebSocket,data){
    let _time = 10//重试10次
    function _sendWebsocket(ws:WebSocket,data) {
        if(_time--<0){
            console.log(_time)
            return;
        }
        if (ws && ws.readyState == ws.OPEN) {
            ws.send(JSON.stringify(data))
        } else {
            setTimeout(function (){_sendWebsocket(ws, data)},5000);
        }
    }
    _sendWebsocket(ws,data)
}