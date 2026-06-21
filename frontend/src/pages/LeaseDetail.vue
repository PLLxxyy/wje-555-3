<template>
  <div v-if="store.current">
    <div class="page-heading"><h1>{{ store.current.propertyTitle }}</h1><LeaseStatusTag :status="store.current.status" /></div>
    <el-descriptions border :column="2">
      <el-descriptions-item label="租客">{{ store.current.tenantName }}</el-descriptions-item>
      <el-descriptions-item label="房东">{{ store.current.landlordName }}</el-descriptions-item>
      <el-descriptions-item label="租期">{{ store.current.startDate }} 至 {{ store.current.endDate }}</el-descriptions-item>
      <el-descriptions-item label="月租">{{ formatMoney(store.current.monthlyRent) }}</el-descriptions-item>
      <el-descriptions-item label="押金">{{ formatMoney(store.current.deposit) }}</el-descriptions-item>
      <el-descriptions-item label="付款周期">{{ enumLabels[store.current.paymentCycle] }}</el-descriptions-item>
    </el-descriptions>
    <section class="plain-section">
      <h2>关联账单</h2>
      <BillTable :bills="store.current.bills || []" @pay="() => undefined" @urge="() => undefined" @waive="() => undefined" />
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import BillTable from '@/components/common/BillTable.vue'
import LeaseStatusTag from '@/components/common/LeaseStatusTag.vue'
import { enumLabels } from '@/constants/enums'
import { useLeaseStore } from '@/stores/leaseStore'
import { formatMoney } from '@/utils/format'

const store = useLeaseStore()
const route = useRoute()
onMounted(() => store.fetchOne(route.params.id as string))
</script>

