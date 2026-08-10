<template>
  <div style="padding:20px">
    <el-button @click="$router.push('/login')">登录</el-button>
    <el-button @click="$router.push('/publish')">发布商品</el-button>
    <el-button @click="$router.push('/mygoods')">我的商品</el-button>
    <h2>全部二手商品</h2>
    <el-row>
      <el-col span="8" v-for="item in goodsList" :key="item.id">
        <el-card>
          <h3>{{item.title}}</h3>
          <p>价格：{{item.price}}</p>
          <p>{{item.desc}}</p>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script setup>
import {ref,onMounted} from 'vue'
import axios from 'axios'
const goodsList = ref([])
const loadData = async ()=>{
  const res = await axios.get("/api/goods")
  goodsList.value = res.data
}
onMounted(()=>loadData())
</script>
