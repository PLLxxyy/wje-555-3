<template>
  <el-tag :type="tagType" effect="light">{{ label }}</el-tag>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { BillStatus, LeaseStatus, PropertyStatus, RepairStatus, billStatusLabels, enumLabels, leaseStatusLabels, propertyStatusLabels, repairStatusLabels } from '@/constants/enums'

const props = defineProps<{ value: string; domain?: 'property' | 'lease' | 'bill' | 'repair' }>()
const label = computed(() => {
  if (props.domain === 'property') return propertyStatusLabels[props.value as PropertyStatus]
  if (props.domain === 'lease') return leaseStatusLabels[props.value as LeaseStatus]
  if (props.domain === 'bill') return billStatusLabels[props.value as BillStatus]
  if (props.domain === 'repair') return repairStatusLabels[props.value as RepairStatus]
  return enumLabels[props.value] || props.value
})
const tagType = computed(() => {
  if ([LeaseStatus.ACTIVE, BillStatus.PAID, RepairStatus.COMPLETED, PropertyStatus.AVAILABLE].includes(props.value as never)) return 'success'
  if ([LeaseStatus.PENDING, BillStatus.PENDING, RepairStatus.PENDING].includes(props.value as never)) return 'warning'
  if ([LeaseStatus.EXPIRED, BillStatus.OVERDUE].includes(props.value as never)) return 'danger'
  return 'info'
})
</script>
