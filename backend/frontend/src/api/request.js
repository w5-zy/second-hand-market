import axios from "axios";

const service = axios.create({
  baseUrl:"/api"
})

export default service
