<template>
  <div v-if="store.current">
    <div class="page-heading">
      <h1>{{ store.current.propertyTitle }}</h1>
      <div class="heading-actions">
        <LeaseStatusTag :status="store.current.status" />
        <el-button
          v-if="isLandlord && store.current.status === LeaseStatus.ACTIVE"
          type="danger"
          plain
          @click="showTerminateDialog = true"
        >
          终止租约
        </el-button>
      </div>
    </div>
    <el-descriptions border :column="2">
      <el-descriptions-item label="租客">{{ store.current.tenantName }}</el-descriptions-item>
      <el-descriptions-item label="房东">{{ store.current.landlordName }}</el-descriptions-item>
      <el-descriptions-item label="租期">{{ store.current.startDate }} 至 {{ store.current.endDate }}</el-descriptions-item>
      <el-descriptions-item label="月租">{{ formatMoney(store.current.monthlyRent) }}</el-descriptions-item>
      <el-descriptions-item label="押金">{{ formatMoney(store.current.deposit) }}</el-descriptions-item>
      <el-descriptions-item label="付款周期">{{ enumLabels[store.current.paymentCycle] }}</el-descriptions-item>
      <el-descriptions-item v-if="store.current.status === LeaseStatus.TERMINATED" label="终止原因">{{ store.current.terminationReason }}</el-descriptions-item>
    </el-descriptions>
    <section class="plain-section">
      <h2>关联账单</h2>
      <BillTable :bills="store.current.bills || []" @pay="() => undefined" @urge="() => undefined" @waive="() => undefined" />
    </section>

    <el-dialog v-model="showTerminateDialog" title="终止租约" width="480px" @close="resetTerminateForm">
      <el-form ref="terminateFormRef" :model="terminateForm" :rules="terminateRules" label-width="100px">
        <el-form-item label="终止原因" prop="terminationReason">
          <el-input v-model="terminateForm.terminationReason" type="textarea" :rows="3" placeholder="请输入终止原因" />
        </el-form-item>
        <el-form-item label="违约金" prop="penaltyAmount">
          <el-input-number v-model="terminateForm.penaltyAmount" :min="0.01" :precision="2" style="width: 100%" />
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
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import BillTable from '@/components/common/BillTable.vue'
import LeaseStatusTag from '@/components/common/LeaseStatusTag.vue'
import { LeaseStatus, enumLabels } from '@/constants/enums'
import { useLeaseStore } from '@/stores/leaseStore'
import { formatMoney } from '@/utils/format'
import { usePermission } from '@/composables/usePermission'

const store = useLeaseStore()
const route = useRoute()
const { isLandlord } = usePermission()

const showTerminateDialog = ref(false)
const terminateFormRef = ref<FormInstance>()
const terminateForm = ref({
  terminationReason: '',
  penaltyAmount: 0.01,
})

const terminateRules: FormRules = {
  terminationReason: [{ required: true, message: '请输入终止原因', trigger: 'blur' }],
  penaltyAmount: [{ type: 'number', min: 0.01, message: '违约金必须大于 0', trigger: 'blur' }],
}

function resetTerminateForm() {
  terminateForm.value = {
    terminationReason: '',
    penaltyAmount: 0.01,
  }
  terminateFormRef.value?.resetFields()
}

async function handleTerminate() {
  if (!store.current) return
  const valid = await terminateFormRef.value?.validate().catch(() => false)
  if (!valid) return
  try {
    await store.terminate(store.current.id, {
      terminationReason: terminateForm.value.terminationReason,
      penaltyAmount: terminateForm.value.penaltyAmount,
    })
    ElMessage.success('租约已终止')
    showTerminateDialog.value = false
  } catch (e) {
    ElMessage.error('终止失败')
  }
}

onMounted(() => store.fetchOne(route.params.id as string))
</script>

<style scoped>
.page-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.heading-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>

