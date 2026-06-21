<template>
  <div>
    <div class="page-heading"><div><h1>账单中心</h1><p>待付、已付、逾期和减免账单集中处理</p></div></div>
    <div class="metric-grid">
      <section><span>待付总额</span><strong>{{ formatMoney(store.stats.pendingTotal) }}</strong></section>
      <section><span>已付总额</span><strong>{{ formatMoney(store.stats.paidTotal) }}</strong></section>
      <section><span>逾期总额</span><strong>{{ formatMoney(store.stats.overdueTotal) }}</strong></section>
    </div>
    <el-tabs v-model="status" @tab-change="load">
      <el-tab-pane label="待付" :name="BillStatus.PENDING" />
      <el-tab-pane label="已付" :name="BillStatus.PAID" />
      <el-tab-pane label="逾期" :name="BillStatus.OVERDUE" />
      <el-tab-pane label="已减免" :name="BillStatus.WAIVED" />
    </el-tabs>
    <BillTable :bills="store.items" @pay="pay" @urge="urge" @waive="waive" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { billApi } from '@/api/bill'
import BillTable from '@/components/common/BillTable.vue'
import { BillStatus } from '@/constants/enums'
import { useBillStore } from '@/stores/billStore'
import type { Bill } from '@/types/bill'
import { formatMoney } from '@/utils/format'

const status = ref(BillStatus.PENDING)
const store = useBillStore()
async function load() { await store.fetch({ status: status.value }); await store.fetchStats() }
onMounted(load)
async function pay(row: Bill) { await billApi.pay(row.id); await load() }
async function urge(row: Bill) { await billApi.urge(row.id); ElMessage.success('催缴提醒已发送') }
async function waive(row: Bill) { await billApi.waive(row.id, { remark: '减免处理' }); await load() }
</script>

