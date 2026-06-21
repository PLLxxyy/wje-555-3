<template>
  <div>
    <div class="page-heading">
      <div>
        <h1>租赁运营总览</h1>
        <p>房源、租约、账单、维修工单集中处理</p>
      </div>
      <el-button type="primary" @click="$router.push('/properties/new')" v-permission="[UserRole.LANDLORD]">发布房源</el-button>
    </div>
    <div class="metric-grid">
      <section><span>在管房源</span><strong>{{ property.items.length }}</strong></section>
      <section><span>租约数量</span><strong>{{ lease.items.length }}</strong></section>
      <section><span>待付账单</span><strong>{{ formatMoney(bill.stats.pendingTotal) }}</strong></section>
      <section><span>维修工单</span><strong>{{ repair.items.length }}</strong></section>
    </div>
    <div class="content-grid">
      <section>
        <h2>推荐房源</h2>
        <div class="cards-grid">
          <PropertyCard v-for="item in property.items.slice(0, 3)" :key="item.id" :property="item" />
        </div>
      </section>
      <section>
        <h2>近期账单</h2>
        <BillTable :bills="bill.items.slice(0, 5)" @pay="payBill" @urge="urgeBill" @waive="waiveBill" />
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import BillTable from '@/components/common/BillTable.vue'
import PropertyCard from '@/components/common/PropertyCard.vue'
import { billApi } from '@/api/bill'
import { UserRole } from '@/constants/enums'
import { useBillStore } from '@/stores/billStore'
import { useLeaseStore } from '@/stores/leaseStore'
import { usePropertyStore } from '@/stores/propertyStore'
import { useRepairStore } from '@/stores/repairStore'
import type { Bill } from '@/types/bill'
import { formatMoney } from '@/utils/format'

const property = usePropertyStore()
const lease = useLeaseStore()
const bill = useBillStore()
const repair = useRepairStore()
onMounted(async () => {
  await Promise.all([property.fetch(), lease.fetch().catch(() => undefined), bill.fetch().catch(() => undefined), bill.fetchStats().catch(() => undefined), repair.fetch().catch(() => undefined)])
})
async function payBill(row: Bill) { await billApi.pay(row.id); await bill.fetch(); ElMessage.success('已标记支付') }
async function urgeBill(row: Bill) { await billApi.urge(row.id); ElMessage.success('已发送催缴') }
async function waiveBill(row: Bill) { await billApi.waive(row.id, { remark: '运营台减免' }); await bill.fetch() }
</script>

