<template>
  <div>
    <div
        ref="line"
        class="line"
        :style="{ top: `${top}px`, left: `${left}px` }"
        @mousedown="startDrag"
    ></div>
    <textarea
        class="text-area"
        :style="{ top: `${top + 2}px`, left: `${left}px`,height:`${initHeight}px`} "
    ></textarea>
  </div>
</template>
<script setup lang="ts">
import {ref, watch} from 'vue';
const line = ref<HTMLElement | null>(null);
const top = ref(100); // 初始纵坐标
const left = ref(0); // 不需要改变横坐标位置
const isDragging = ref(false);
const initialMouseY = ref(0);
const initialTop = ref(0);
const initHeight = ref(window.innerHeight - top.value - 15)
const startDrag = (event: MouseEvent) => {
  isDragging.value = true;
  initialMouseY.value = event.clientY; // 记录初始鼠标的纵坐标
  initialTop.value = top.value; // 记录初始纵坐标
  window.addEventListener('mousemove', drag);
  window.addEventListener('mouseup', stopDrag);
};
watch(top, (newTop) => {
  initHeight.value = window.innerHeight - newTop - 15
})
const drag = (event: MouseEvent) => {
  if (isDragging.value) {
    const deltaY = event.clientY - initialMouseY.value; // 计算鼠标移动的距离
    if (initialTop.value + deltaY < window.innerHeight) {
      top.value = initialTop.value + deltaY; // 更新纵坐标
      // 更新 CSS 变量
      document.documentElement.style.setProperty('--line-top', `${top.value}px`);
    }
  }
};
const stopDrag = () => {
  isDragging.value = false;
  window.removeEventListener('mousemove', drag);
  window.removeEventListener('mouseup', stopDrag);
};
</script>

<style scoped lang="scss">
.line {
  position: absolute; /* 使用绝对定位 */
  width: 100%; /* 设置宽度为100% */
  height: 0; /* 不需要设置高度，边框会产生线的效果 */
  border-top: 2px solid black; /* 修正边框属性 */
  transform: translateY(-50%); /* 使线条中心在鼠标位置 */
  cursor: s-resize; /* 鼠标指针样式 */
  z-index: 10; /* 确保线在textarea之上 */
  padding: 0;
  margin: 0;
}
.line:hover {
  box-shadow: 0 0 10px rgba(255, 215, 0, 0.8), /* 发光效果 */
              0 0 20px rgba(255, 215, 0, 0.6); /* 可以根据需要调整颜色和模糊度 */
}
.text-area {
  position: absolute; /* 使用绝对定位 */
  width: 99.98%; /* 设置宽度为100% */
  top: calc(var(--line-top) + 2px); /* 使用 CSS 变量来动态调整位置 */
  left: 0; /* 确保左侧位置为0 */
  border: 1px solid #ccc; /* 设置边框 */
  resize: none; /* 禁用调整大小 */
  z-index: 1; /* textarea 在下方 */
  background: #cccccc;
  padding: 0;
  margin: 0;
}
</style>
