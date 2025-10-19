import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

//think of this as training a messenger owl to communicate 
//between backend and frontend

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL 
});//this api is like giving the message owl the adress of the backend server

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN); //you gotta get the acces token bro!
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; //making the jwt token !
    }
    return config;
    //what actually is config ? think of config as the message which stores 
    // the data , id , authorization header,the method and url
  },
  (error) => {
    return Promise.reject(error);//typical error catching
  }
);

export default api;