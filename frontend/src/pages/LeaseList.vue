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
          <el-button
            v-if="isLandlord && row.status === LeaseStatus.ACTIVE"
            size="small"
            type="danger"
            plain
            @click.stop="openTerminateDialog(row)"
          >
            终止
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="showTerminateDialog" title="终止租约" width="480px" @close="resetTerminateForm">
      <el-form ref="terminateFormRef" :model="terminateForm" :rules="terminateRules" label-width="100px">
        <el-form-item label="终止原因" prop="terminationReason">
          <el-input v-model="terminateForm.terminationReason" type="textarea" :rows="3" placeholder="请输入终止原因" />
        </el-form-item>
        <el-form-item label="违约金" prop="penaltyAmount">
          <el-input-number v-model="terminateForm.penaltyAmount" :min="0" :precision="2" style="width: 100%" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="showTerminateDialog = false">取消</el-button>
        <el-button type="danger" @click="handleTerminate">确认终止</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import { leaseApi } from '@/api/lease'
import LeaseStatusTag from '@/components/common/LeaseStatusTag.vue'
import { LeaseStatus, enumLabels } from '@/constants/enums'
import { usePermission } from '@/composables/usePermission'
import { useLeaseStore } from '@/stores/leaseStore'
import type { Lease } from '@/types/lease'

const store = useLeaseStore()
const { isLandlord, isTenant } = usePermission()
const roleText = computed(() => isLandlord.value ? '我发起的租约' : isTenant.value ? '我的租约' : '全部租约')
onMounted(() => store.fetch())
async function sign(row: Lease) { await leaseApi.sign(row.id); await store.fetch() }

const showTerminateDialog = ref(false)
const terminateFormRef = ref<FormInstance>()
const currentRow = ref<Lease | null>(null)
const terminateForm = ref({
  terminationReason: '',
  penaltyAmount: 0,
})

const terminateRules: FormRules = {
  terminationReason: [{ required: true, message: '请输入终止原因', trigger: 'blur' }],
  penaltyAmount: [{ type: 'number', min: 0, message: '违约金不能为负数', trigger: 'blur' }],
}

function resetTerminateForm() {
  terminateForm.value = {
    terminationReason: '',
    penaltyAmount: 0,
  }
  currentRow.value = null
  terminateFormRef.value?.resetFields()
}

function openTerminateDialog(row: Lease) {
  currentRow.value = row
  showTerminateDialog.value = true
}

async function handleTerminate() {
  if (!currentRow.value) return
  const valid = await terminateFormRef.value?.validate().catch(() => false)
  if (!valid) return
  try {
    await leaseApi.terminate(currentRow.value.id, {
      terminationReason: terminateForm.value.terminationReason,
      penaltyAmount: terminateForm.value.penaltyAmount,
    })
    ElMessage.success('租约已终止')
    showTerminateDialog.value = false
    await store.fetch()
  } catch (e) {
    ElMessage.error('终止失败')
  }
}
</script>

