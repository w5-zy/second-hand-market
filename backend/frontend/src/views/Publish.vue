<template>
  <el-card style="width:500px;margin:50px auto;">
    <h2>发布二手商品</h2>
    <el-input v-model="goods.title" placeholder="商品名称"></el-input>
    <el-input v-model.number="goods.price" placeholder="价格"></el-input>
    <el-input v-model="goods.desc" type="textarea" placeholder="商品描述"></el-input>
    <el-button @click="submit">提交发布</el-button>
  </el-card>
</template>
<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const router = useRouter()
const goods = ref({title:'',price:0,desc:''})
const submit = async ()=>{
  const uid = localStorage.getItem("uid")
  if(!uid){
    alert("请先登录")
    router.push("/login")
    return
  }
  await axios.post(`/api/goods?uid=${uid}`,goods.value)
  alert("发布成功")
  router.push("/")
}
</script>
