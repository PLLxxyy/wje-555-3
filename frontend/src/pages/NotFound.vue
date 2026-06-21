<template>
  <EmptyState description="页面不存在">
    <el-button type="primary" @click="$router.push('/')">返回总览</el-button>
  </EmptyState>
</template>

<script setup lang="ts">
import EmptyState from '@/components/common/EmptyState.vue'
</script>

