<template>
  <StatusBadge :value="status" domain="lease" />
</template>

<script setup lang="ts">
import StatusBadge from './StatusBadge.vue'
import type { LeaseStatus } from '@/constants/enums'

defineProps<{ status: LeaseStatus }>()
</script>
