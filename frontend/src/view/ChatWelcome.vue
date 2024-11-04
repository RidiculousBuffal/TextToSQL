<template>
  <div class="welcome-container">
    <img :src="logoUrl" alt="Logo" class="logo" />
    <h1 class="welcome-title">Welcome to LLM toolbox!</h1>
    <button class="experience-button" @click="handleExperienceClick">SQL 工具箱</button>
    <button class="experience-button" @click="handleDify">Dify 应用展示</button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { Brand_URL } from '@/const/figure.ts';
import {useRouter} from "vue-router";
import { v4 as uuidv4 } from 'uuid';
const logoUrl = ref(Brand_URL);
const router = useRouter()
const handleExperienceClick = () => {
  router.push('/chat')
};
const handleDify = ()=>{
  router.push('/dify')
}
import {userToken} from "@/store/UserToken";
// 判断是不是第一次进入
const useUserToken = userToken()
if(useUserToken.token==undefined){
  const uuid:uuidv4 = uuidv4()
   useUserToken.setToken(uuid)
  console.log(uuid)
}

</script>

<style scoped>
.welcome-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f9f9f9; /* 浅色背景 */
  text-align: center;
}

.logo {
  width: 300px; /* 根据需要调整 logo 的大小 */
  margin-bottom: 20px;
}

.welcome-title {
  font-size: 24px;
  color: #333; /* 深色文字 */
  margin-bottom: 20px;
}

.experience-button {
  padding: 12px 25px;
  background: rgb(247, 207, 174); /* 渐变背景 */
  color: #f8efef;
  border: none;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s, transform 0.3s; /* 添加平滑过渡效果 */
}

.experience-button:hover {
  background:  rgb(247, 207, 174); /* 更深的渐变色 */
  transform: scale(1.05); /* 鼠标悬停时放大按钮 */
}
</style>
