<template>
  <div class="chat-message" :class="{'user-message': isUser, 'assistant-message': !isUser}">
    <div class="avatar" :class="{'user-avatar': isUser, 'assistant-avatar': !isUser}">
      <img :src="isUser ? USER_LOGO : GPT_LOGO" alt="Avatar" />
    </div>
    <div class="content">
      <VueMarkdown :source="content" :plugins="plugins"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, computed } from 'vue';
import ChatModel from "@/typeutils/ChatModel"; // 确保路径正确
import { GPT_LOGO, USER_LOGO } from "@/const/figure"; // 确保路径正确
import VueMarkdown from 'vue-markdown-render';
import MarkdownItKatex from 'markdown-it-katex';

const plugins = [MarkdownItKatex];
const props = defineProps<ChatModel>();

// 计算属性判断用户角色
const isUser = computed(() => props.role === 'user');

</script>

<style scoped lang="scss">
.chat-message {
  display: flex;
  align-items: flex-start;
  margin: 10px 0;

  &.user-message {
    flex-direction: row-reverse; // 用户消息时头像在右侧
  }

  .avatar {
    margin-right: 10px; // 默认左侧头像的间距
    img {
      width: 40px; // 根据需要设置头像大小
      height: 40px;
      border-radius: 50%; // 圆形头像
    }
  }

  .content {
    background-color: #f1f1f1; // 消息背景颜色
    padding: 10px;
    border-radius: 8px;
    max-width: 70%; // 控制消息内容的最大宽度
    overflow: auto;
    word-wrap: break-word; // 处理长单词换行
  }

  &.assistant-message .content {
    background-color: #e0f7fa; // 更改AI助手消息的背景颜色
  }

  &.user-message .content {
    background-color: #ffe0b2; // 更改用户消息的背景颜色
  }
}
</style>
