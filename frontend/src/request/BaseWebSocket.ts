import type {AllowedEndpoint} from "@/typeutils/availableEndPoint";
const BASE_URL = import.meta.env.VITE_APP_BACKEND_URL
export default function (endpoint:AllowedEndpoint){
    console.log(BASE_URL)
    return new WebSocket(`ws://localhost:8000${endpoint}`)
}