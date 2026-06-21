<template>
  <div class="image-uploader">
    <el-input v-model="url" placeholder="粘贴图片 URL" @keyup.enter="add" />
    <el-button @click="add">添加</el-button>
    <div class="image-strip">
      <el-tag v-for="(item, index) in modelValue" :key="item" closable @close="remove(index)">{{ item }}</el-tag>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{ modelValue: string[] }>()
const emit = defineEmits<{ 'update:modelValue': [string[]] }>()
const url = ref('')
function add() {
  if (!url.value) return
  emit('update:modelValue', [...props.modelValue, url.value])
  url.value = ''
}
function remove(index: number) {
  emit('update:modelValue', props.modelValue.filter((_, i) => i !== index))
}
</script>

