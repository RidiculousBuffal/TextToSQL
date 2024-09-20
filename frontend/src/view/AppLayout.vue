<!-- APPLAYOUT.vue -->
<script setup lang="ts">
import SQLTables from "@/component/SQLTables.vue";
import ChatWithSQL from "@/component/ChatWithSQL.vue";
</script>

<template>
  <div class="layout-container">
    <ChatWithSQL class="chat-with-sql" />
    <SQLTables class="sql-tables" />
  </div>
</template>

<style scoped lang="scss">
.layout-container {
  display: flex; /* 使用 Flexbox 排列子组件 */
  height: 100vh; /* 使容器高度占满整个屏幕 */
  margin: 0;
}

.chat-with-sql {
  flex: 0 0 80%; /* 设定 ChatWithSQL 占据 80% */
  background-color: #f0f0f0; /* 可选，设置背景颜色以便于视觉区分 */
}

.sql-tables {
  flex: 0 0 20%; /* 设定 SQLTables 占据 20% */
  background-color: #e0e0e0; /* 可选，设置背景颜色以便于视觉区分 */
}
</style>
