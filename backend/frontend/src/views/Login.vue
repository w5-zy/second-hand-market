<template>
  <el-card style="width:400px;margin:100px auto;">
    <h2>登录/注册</h2>
    <el-input v-model="form.username" placeholder="用户名"></el-input>
    <el-input v-model="form.password" placeholder="密码" type="password"></el-input>
    <el-button @click="handleRegister">注册</el-button>
    <el-button @click="handleLogin">登录</el-button>
  </el-card>
</template>
<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const router = useRouter()
const form = ref({username:'',password:''})

const handleRegister = async ()=>{
  await axios.post("/api/user/register",form.value)
  alert("注册成功，请登录")
}
const handleLogin = async ()=>{
  const res = await axios.post("/api/user/login",form.value)
  localStorage.setItem("uid",res.data.uid)
  router.push("/")
}
</script>
