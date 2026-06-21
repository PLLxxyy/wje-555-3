<template>
  <el-timeline>
    <el-timeline-item v-for="item in items" :key="item.id" :timestamp="formatDate(item.createdAt)">
      {{ item.action }} · {{ item.actorName || '系统' }}
    </el-timeline-item>
  </el-timeline>
</template>

<script setup lang="ts">
import { formatDate } from '@/utils/format'

defineProps<{ items: Array<{ id: string; action: string; actorName?: string; createdAt: string }> }>()
</script>

