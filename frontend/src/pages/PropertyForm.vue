<template>
  <div>
    <div class="page-heading"><h1>{{ isEdit ? '编辑房源' : '发布房源' }}</h1></div>
    <el-form :model="form" label-position="top" class="form-grid">
      <el-form-item label="标题"><el-input v-model="form.title" /></el-form-item>
      <el-form-item label="类型"><el-select v-model="form.type"><el-option v-for="item in Object.values(PropertyType)" :key="item" :label="enumLabels[item]" :value="item" /></el-select></el-form-item>
      <el-form-item label="地址"><el-input v-model="form.address" /></el-form-item>
      <el-form-item label="户型"><el-input v-model="form.rooms" /></el-form-item>
      <el-form-item label="面积"><el-input-number v-model="form.area" :min="1" /></el-form-item>
      <el-form-item label="楼层"><el-input-number v-model="form.floor" /></el-form-item>
      <el-form-item label="总楼层"><el-input-number v-model="form.totalFloors" /></el-form-item>
      <el-form-item label="月租"><el-input-number v-model="form.price" :min="0" /></el-form-item>
      <el-form-item label="押金"><el-input-number v-model="form.deposit" :min="0" /></el-form-item>
      <el-form-item label="图片"><ImageUploader v-model="form.images" /></el-form-item>
      <el-form-item label="设施"><el-select v-model="form.facilities" multiple><el-option v-for="item in facilities" :key="item" :label="item" :value="item" /></el-select></el-form-item>
      <el-form-item label="描述" class="span-2"><el-input v-model="form.description" type="textarea" :rows="4" /></el-form-item>
      <el-button type="primary" @click="submit">保存</el-button>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ImageUploader from '@/components/common/ImageUploader.vue'
import { propertyApi } from '@/api/property'
import { PropertyStatus, PropertyType, enumLabels } from '@/constants/enums'

const route = useRoute()
const router = useRouter()
const isEdit = computed(() => Boolean(route.params.id))
const facilities = ['空调', '洗衣机', '冰箱', '宽带', '热水器', '燃气', '电梯']
const form = reactive({
  title: '', type: PropertyType.WHOLE, address: '', rooms: '2室1厅1卫', area: 80, floor: 8, totalFloors: 24,
  price: 5000, deposit: 5000, status: PropertyStatus.AVAILABLE, images: [] as string[], facilities: ['空调', '宽带'],
  description: '', latitude: '30.208400', longitude: '120.212000',
})
onMounted(async () => {
  if (isEdit.value) Object.assign(form, await propertyApi.detail(route.params.id as string))
})
async function submit() {
  if (isEdit.value) await propertyApi.update(route.params.id as string, form)
  else await propertyApi.create(form)
  router.push('/properties')
}
</script>

