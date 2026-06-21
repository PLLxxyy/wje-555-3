<template>
  <div v-if="property.current">
    <div class="detail-hero">
      <el-carousel height="320px">
        <el-carousel-item v-for="image in property.current.images" :key="image"><img :src="image" /></el-carousel-item>
      </el-carousel>
      <section>
        <StatusBadge :value="property.current.status" domain="property" />
        <h1>{{ property.current.title }}</h1>
        <strong>{{ formatMoney(property.current.price) }}/月</strong>
        <p>{{ property.current.rooms }} · {{ property.current.area }}㎡ · {{ property.current.floor }}/{{ property.current.totalFloors }}层</p>
        <p>{{ property.current.address }}</p>
        <div class="tag-row"><el-tag v-for="item in property.current.facilities" :key="item">{{ item }}</el-tag></div>
        <div class="action-row">
          <el-button type="primary" v-permission="[UserRole.TENANT]">预约看房</el-button>
          <el-button v-permission="[UserRole.LANDLORD]" @click="$router.push(`/properties/${property.current?.id}/edit`)">编辑</el-button>
          <el-button v-permission="[UserRole.LANDLORD]" @click="toggleStatus">上架/维护</el-button>
          <el-button v-permission="[UserRole.LANDLORD]" type="danger" plain @click="remove">删除</el-button>
        </div>
      </section>
    </div>
    <section class="plain-section">
      <h2>房源描述</h2><p>{{ property.current.description }}</p>
      <h2>周边信息</h2><p>地铁站步行约 8 分钟，周边覆盖超市、学校、社区医院和商业街。</p>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { propertyApi } from '@/api/property'
import StatusBadge from '@/components/common/StatusBadge.vue'
import { PropertyStatus, UserRole } from '@/constants/enums'
import { usePropertyStore } from '@/stores/propertyStore'
import { formatMoney } from '@/utils/format'

const route = useRoute()
const router = useRouter()
const property = usePropertyStore()
onMounted(() => property.fetchOne(route.params.id as string))
async function toggleStatus() {
  const next = property.current?.status === PropertyStatus.MAINTENANCE ? PropertyStatus.AVAILABLE : PropertyStatus.MAINTENANCE
  await propertyApi.setStatus(route.params.id as string, next)
  await property.fetchOne(route.params.id as string)
}
async function remove() {
  await propertyApi.remove(route.params.id as string)
  router.push('/properties')
}
</script>
