<script lang="ts" setup>
import {ref} from 'vue';
import ChatDialog from "@/chatUI/chatDialog.vue";
import type ChatModel from "@/typeutils/ChatModel";
import {MyNotification} from "@/utils/Notification";
import {areAllPropertiesDefined} from "@/utils/someTools";
import type DBConnector from "@/typeutils/DBConnector";
import {DBToken} from "@/store/DBToken";
import baseWebSocket from "@/request/BaseWebSocket";
import {SQLworkflow} from "@/workflow/SQLWorkFlow";
// 示例消息数据
const messages = ref<Array<ChatModel>>([]);

const userInput = ref("");
const wsServer = baseWebSocket('/chatWithSQL')
wsServer.addEventListener('message', (event) => {
      const data_ = JSON.parse(JSON.parse(event.data))
      SQLworkflow(data_, messages)
    }
);
wsServer.addEventListener('close', (event) => {
  MyNotification("success", '本次对话结束', "Over")
  wsServer.close()
})
type databaseSend = {
  userQuery: string,
  databaseName: string
}

const sendMessage = () => {
  if (userInput.value.trim()) {
    const dbTokenStore = DBToken()
    const dbtoken: DBConnector = dbTokenStore.DBToken;
    const userMessage: ChatModel = {
      role: 'user',
      content: userInput.value
    }
    if (areAllPropertiesDefined(dbtoken)) {
      messages.value.push(userMessage);
      userInput.value = '';
      const send: databaseSend = {
        userQuery: userMessage.content,
        databaseName: dbtoken.DB_NAME
      }
      wsServer.send(JSON.stringify(send))
      messages.value.push({role: 'assistant', 'content': ''})
    } else {
      MyNotification("error", "请先连接到数据库并选择database", "出错啦!")
    }

  }
};
</script>
<template>
  <div class="container">
    <h1>Chat Dialog Test</h1>
    <div class="chat-container">
      <ChatDialog v-for="(message, index) in messages" :key="index" :role="message.role" :content="message.content"/>
    </div>

    <div class="input-area">
      <textarea
          v-model="userInput"
          placeholder="Type your message here..."
          class="input-box"
          rows="4"
      ></textarea>

      <el-button
          type="primary"
          class="send-button"
          @click="sendMessage">
        Send
      </el-button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  max-width: 100%;
  margin: 0 auto;
  padding: 20px;
  height: 100vh; /* 设置为全高 */
  display: flex;
  flex-direction: column; /* 纵向排列 */
}

h1 {
  margin-bottom: 10px; /* 与聊天区域的间距 */
}

.chat-container {
  flex: 1; /* 占据剩余空间，约 80% */
  overflow-y: auto; /* 允许垂直滚动 */
}

.input-area {
  height: 20%; /* 固定输入区域和按钮的高度为 20% */
  display: flex; /* 水平排列输入框和按钮 */

  flex-direction: column;
}

.input-box {

  background-color: transparent; /* 背景透明 */
  border-top: 1px dashed black; /* 虚线黑色上边框 */
  border-left: 0;
  border-right: 0;
  border-bottom: 0;
  height: 80%;
  box-shadow: none; /* 移除阴影 */
  resize: none; /* 禁用拉伸 */
  font-size: 16px; /* 字体大小 */
  padding: 10px; /* 内边距 */
  outline: none; /* 移除焦点外边框 */
}

.send-button {
  margin-left: auto;
  height: 40px;
}
</style>
