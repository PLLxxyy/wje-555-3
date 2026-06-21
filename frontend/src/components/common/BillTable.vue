<template>
  <el-table :data="bills" class="bill-table">
    <el-table-column prop="title" label="账单" min-width="180" />
    <el-table-column label="类型" width="96">
      <template #default="{ row }"><el-tag>{{ enumLabels[row.type] }}</el-tag></template>
    </el-table-column>
    <el-table-column label="金额" width="120">
      <template #default="{ row }">{{ formatMoney(row.amount) }}</template>
    </el-table-column>
    <el-table-column label="应付日期" width="120">
      <template #default="{ row }">{{ formatDate(row.dueDate) }}</template>
    </el-table-column>
    <el-table-column label="状态" width="100">
      <template #default="{ row }"><StatusBadge :value="row.status" domain="bill" /></template>
    </el-table-column>
    <el-table-column label="操作" width="220">
      <template #default="{ row }">
        <el-button size="small" type="primary" plain @click.stop="$emit('pay', row)" v-permission="[UserRole.TENANT]">支付</el-button>
        <el-button size="small" plain @click.stop="$emit('urge', row)" v-permission="[UserRole.LANDLORD]">催缴</el-button>
        <el-button size="small" plain @click.stop="$emit('waive', row)" v-permission="[UserRole.LANDLORD]">减免</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup lang="ts">
import StatusBadge from './StatusBadge.vue'
import { UserRole, enumLabels } from '@/constants/enums'
import type { Bill } from '@/types/bill'
import { formatDate, formatMoney } from '@/utils/format'

defineProps<{ bills: Bill[] }>()
defineEmits<{ pay: [Bill]; urge: [Bill]; waive: [Bill] }>()
</script>
