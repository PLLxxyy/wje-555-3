<template>
  <div>
    <div class="page-heading"><h1>提交报修</h1></div>
    <el-form :model="form" label-position="top" class="form-grid">
      <el-form-item label="房源 ID"><el-input v-model="form.property_id" /></el-form-item>
      <el-form-item label="优先级"><el-select v-model="form.priority"><el-option v-for="item in Object.values(RepairPriority)" :key="item" :label="enumLabels[item]" :value="item" /></el-select></el-form-item>
      <el-form-item label="标题"><el-input v-model="form.title" /></el-form-item>
      <el-form-item label="图片"><ImageUploader v-model="form.images" /></el-form-item>
      <el-form-item label="描述" class="span-2"><el-input v-model="form.description" type="textarea" :rows="5" /></el-form-item>
      <el-button type="primary" @click="submit">提交</el-button>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { repairApi } from '@/api/repair'
import ImageUploader from '@/components/common/ImageUploader.vue'
import { RepairPriority, enumLabels } from '@/constants/enums'

const router = useRouter()
const form = reactive({ property_id: '', title: '', description: '', images: [] as string[], priority: RepairPriority.MEDIUM })
async function submit() {
  await repairApi.create(form)
  router.push('/repairs')
}
</script>

