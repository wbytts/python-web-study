/**
 * @Description:
 * @FilePath: /admin-ui/src/utils/axios-request.js
 * @**************************************************
 * @Author: BingYi
 * @Date: 2022-07-18 03:05:09
 * @LastEditors: BingYi
 * @LastEditTime: 2022-07-20 15:19:27
 * @good good study π, day day up βοΈ.
 */
import axios from 'axios';

const service = axios.create({
  baseURL: '',
});

// θ―·ζ±ζ¦ζͺε¨
service.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// εεΊζ¦ζͺε¨
service.interceptors.response.use(
  response => {
    return response.data;
  },
  error => {
    return Promise.reject(error);
  }
);

export default service;
