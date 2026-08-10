<template>
<div style="padding:20px">
  <h2>我发布的商品</h2>
  <el-card v-for="g in myList" :key="g.id">
    <h3>{{g.title}}</h3>
    <p>价格{{g.price}}</p>
    <p>{{g.desc}}</p>
  </el-card>
</div>
</template>
<script setup>
import {ref,onMounted} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const router = useRouter()
const myList = ref([])
onMounted(async ()=>{
  const uid = localStorage.getItem("uid")
  if(!uid){
    router.push("/login")
    return
  }
  const res = await axios.get(`/api/goods/me?uid=${uid}`)
  myList.value = res.data
})
</script>
