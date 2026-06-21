<template>
  <div>
    <div class="page-heading"><div><h1>租约管理</h1><p>{{ roleText }}</p></div></div>
    <el-table :data="store.items" @row-click="(row: Lease) => $router.push(`/leases/${row.id}`)">
      <el-table-column prop="propertyTitle" label="房源" min-width="180" />
      <el-table-column prop="tenantName" label="租客" />
      <el-table-column prop="landlordName" label="房东" />
      <el-table-column label="周期"><template #default="{ row }">{{ enumLabels[row.paymentCycle] }}</template></el-table-column>
      <el-table-column label="状态"><template #default="{ row }"><LeaseStatusTag :status="row.status" /></template></el-table-column>
      <el-table-column label="操作" width="240">
        <template #default="{ row }">
          <el-button size="small" @click.stop="sign(row)">签约</el-button>
          <el-button size="small" @click.stop="terminate(row)">终止</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { ElMessageBox } from 'element-plus'
import { leaseApi } from '@/api/lease'
import LeaseStatusTag from '@/components/common/LeaseStatusTag.vue'
import { enumLabels } from '@/constants/enums'
import { usePermission } from '@/composables/usePermission'
import { useLeaseStore } from '@/stores/leaseStore'
import type { Lease } from '@/types/lease'

const store = useLeaseStore()
const { isLandlord, isTenant } = usePermission()
const roleText = computed(() => isLandlord.value ? '我发起的租约' : isTenant.value ? '我的租约' : '全部租约')
onMounted(() => store.fetch())
async function sign(row: Lease) { await leaseApi.sign(row.id); await store.fetch() }
async function terminate(row: Lease) {
  const reason = await ElMessageBox.prompt('填写终止原因', '终止租约')
  await leaseApi.terminate(row.id, reason.value)
  await store.fetch()
}
</script>

