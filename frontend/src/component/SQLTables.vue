<script lang="ts" setup>
import {ref} from "vue";
import {checkDBConnection} from "../../api/db";
import {DBToken} from "@/store/DBToken";
import DBConnector from "@/typeutils/DBConnector";
import {ElNotification} from "element-plus";
import {MyNotification} from "@/utils/Notification";

const DBS = ref<string[]>([]);
const loading = ref(false);
const step = ref<number>(1);
const formValue = ref<DBConnector>({});
const dbTokenStore = DBToken();

const connectToDatabase = async () => {
  loading.value = true;
  const result = await checkDBConnection(formValue.value);
  if (result.status == '1') {
    MyNotification("success", result.message, "链接成功!");
    dbTokenStore.setDBToken(formValue.value);
    console.log(dbTokenStore.DBToken)
    step.value = step.value + 1;
    DBS.value = result.payload;
  } else {
    MyNotification("error", result.message, "失败!");
  }
  loading.value = false;
};
const onhandleChange = (val) => {
  dbTokenStore.setDBToken({
    ...dbTokenStore.DBToken,
    DB_NAME: val,
  })
}
// 页面加载时判断
const checkWhenStart = async () => {
  console.log(dbTokenStore.DBToken)
  if (dbTokenStore.DBToken != undefined) {
    const result = await checkDBConnection(dbTokenStore.DBToken);
    if (result.status == '1') {
      step.value = step.value + 1;
      DBS.value = result.payload;
    }
  }
};
checkWhenStart();
</script>

<template>
  <Transition name="slide-fade">
    <div class="container" v-show="step === 1" v-loading="loading">
      <div class="title">
        <h1>Connect To Your Database</h1>
      </div>
      <div class="form">
        <el-form :model="formValue" label-position="top" class="sql-form">
          <el-form-item label="DB HOST:">
            <el-input v-model="formValue.DB_URL" placeholder="Enter your DB HOST"></el-input>
          </el-form-item>
          <el-form-item label="DB Port:">
            <el-input v-model="formValue.DB_PORT" placeholder="Enter your DB Port"></el-input>
          </el-form-item>
          <el-form-item label="DB Username:">
            <el-input v-model="formValue.DB_USERNAME" placeholder="Enter your DB Username"></el-input>
          </el-form-item>
          <el-form-item label="DB Password:">
            <el-input type="password" v-model="formValue.DB_PASSWORD" placeholder="Enter your DB Password"></el-input>
          </el-form-item>
          <!-- 添加连接按钮 -->
          <el-form-item class="button-item">
            <el-button class="connect-button" @click="connectToDatabase">CONNECT</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </Transition>
  <Transition name="slide-fade">
    <div class="container" v-show="step === 2">
      <el-button type="info" @click="step--" class="back-button">Back</el-button>
      <div class="title">
        <h1>Choose your database</h1>
      </div>
      <div class="choiceBox">
        <el-select
            v-model="formValue.DB_NAME"
            placeholder="Select"
            size="large"
            class="db-select"
            @change='onhandleChange'
        >
          <el-option
              v-for="item in DBS"
              :key="item"
              :label="item"
              :value="item"
          />
        </el-select>
      </div>
    </div>
  </Transition>
</template>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center; /* 水平居中 */
  height: 100vh; /* 使容器高度占满整个视口 */
  background-color: #f9f9f9; /* 背景颜色 */
  padding: 20px; /* 内边距 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* 阴影效果 */
}

.title {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  text-align: center; /* 确保文本在多行时居中 */
  width: 100%; /* 使标题占满整个宽度 */
  margin-bottom: 20px; /* 标题与表单之间的间距 */
}

.form {
  width: 100%; /* 使表单占满宽度 */
  max-width: 400px; /* 限制表单宽度 */
  font-family: "Times New Roman";
  font-weight: 600;
}

.sql-form {
  margin: 10px;
  background-color: #ffffff; /* 表单背景颜色 */
  border-radius: 10px; /* 圆角 */
  padding: 20px; /* 内边距 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 阴影效果 */
}

.el-form-item {
  margin-bottom: 15px; /* 表单项之间的间距 */
}

.button-item {
  text-align: center; /* 按钮项居中 */
}

.connect-button {
  background-color: white; /* 按钮背景色 */
  color: #409EFF; /* 按钮文字颜色 */
  border: 1px solid #409EFF; /* 按钮边框颜色 */
  width: 100%; /* 按钮宽度占满容器 */
  border-radius: 5px; /* 按钮圆角 */
  transition: background-color 0.3s, color 0.3s; /* 添加过渡效果 */

  &:hover {
    background-color: #409EFF; /* 悬停时的背景颜色 */
    color: white; /* 悬停时的文字颜色 */
  }
}

.back-button {
  margin-bottom: 20px; /* "Back" 按钮底部边距 */
  align-self: flex-start; /* 将按钮对齐到左侧 */
}

.choiceBox {
  margin-top: 20px; /* 选择框与标题之间的间距 */
}

.db-select {
  width: 250px; /* 选择框宽度 */
}

/* 定义过渡效果 */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}


.slide-fade-enter-from {
  transform: translateX(20px);
  opacity: 0;
}
</style>
