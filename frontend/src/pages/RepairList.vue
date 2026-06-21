<template>
  <div>
    <div class="page-heading">
      <div><h1>维修工单</h1><p>{{ isTenant ? '我的报修列表' : '待处理与已处理记录' }}</p></div>
      <el-button type="primary" @click="$router.push('/repairs/new')" v-permission="[UserRole.TENANT]">提交报修</el-button>
    </div>
    <el-table :data="store.items">
      <el-table-column prop="title" label="标题" min-width="180" />
      <el-table-column prop="propertyTitle" label="房源" />
      <el-table-column label="优先级"><template #default="{ row }"><el-tag>{{ enumLabels[row.priority] }}</el-tag></template></el-table-column>
      <el-table-column label="状态"><template #default="{ row }"><StatusBadge :value="row.status" domain="repair" /></template></el-table-column>
      <el-table-column prop="assignedTo" label="维修人员" />
      <el-table-column label="操作" width="280">
        <template #default="{ row }">
          <el-button size="small" @click="assign(row)" v-permission="[UserRole.LANDLORD]">派单</el-button>
          <el-button size="small" @click="progress(row)" v-permission="[UserRole.LANDLORD]">维修中</el-button>
          <el-button size="small" type="primary" plain @click="complete(row)">完工</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { ElMessageBox } from 'element-plus'
import { repairApi } from '@/api/repair'
import StatusBadge from '@/components/common/StatusBadge.vue'
import { UserRole, enumLabels } from '@/constants/enums'
import { usePermission } from '@/composables/usePermission'
import { useRepairStore } from '@/stores/repairStore'
import type { RepairOrder } from '@/types/repair'

const store = useRepairStore()
const { isTenant } = usePermission()
onMounted(() => store.fetch())
async function assign(row: RepairOrder) {
  const result = await ElMessageBox.prompt('维修人员姓名/联系方式', '派单')
  await repairApi.assign(row.id, result.value)
  await store.fetch()
}
async function progress(row: RepairOrder) { await repairApi.progress(row.id); await store.fetch() }
async function complete(row: RepairOrder) { await repairApi.complete(row.id, '已完工确认'); await store.fetch() }
</script>
