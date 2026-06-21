<template>
  <div>
    <div class="page-heading">
      <div><h1>房源列表</h1><p>筛选、排序并切换卡片/列表/地图视图</p></div>
      <el-button type="primary" @click="$router.push('/properties/new')" v-permission="[UserRole.LANDLORD]">发布房源</el-button>
    </div>
    <el-form class="filters" :inline="true" :model="filters">
      <el-select v-model="filters.type" placeholder="类型" clearable><el-option v-for="item in propertyTypes" :key="item" :label="enumLabels[item]" :value="item" /></el-select>
      <el-select v-model="filters.status" placeholder="状态" clearable><el-option v-for="item in propertyStatuses" :key="item" :label="enumLabels[item]" :value="item" /></el-select>
      <el-input v-model="filters.min_price" placeholder="最低价" />
      <el-input v-model="filters.max_price" placeholder="最高价" />
      <el-input v-model="filters.rooms" placeholder="户型关键字" />
      <el-select v-model="filters.ordering" placeholder="排序"><el-option label="价格升序" value="price" /><el-option label="价格降序" value="-price" /><el-option label="最新发布" value="-createdAt" /></el-select>
      <el-button @click="load">筛选</el-button>
    </el-form>
    <el-segmented v-model="view" :options="['卡片视图', '列表视图', '地图视图']" />
    <div v-if="view === '卡片视图'" class="cards-grid spacious">
      <PropertyCard v-for="item in store.items" :key="item.id" :property="item" />
    </div>
    <el-table v-else-if="view === '列表视图'" :data="store.items"><el-table-column prop="title" label="房源" /><el-table-column prop="rooms" label="户型" /><el-table-column prop="price" label="月租" /><el-table-column label="状态"><template #default="{ row }"><StatusBadge :value="row.status" domain="property" /></template></el-table-column></el-table>
    <div v-else class="map-panel">
      <strong>静态地图分布</strong>
      <span v-for="item in store.items" :key="item.id">{{ item.title }} · {{ item.latitude }},{{ item.longitude }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import PropertyCard from '@/components/common/PropertyCard.vue'
import StatusBadge from '@/components/common/StatusBadge.vue'
import { PropertyStatus, PropertyType, UserRole, enumLabels } from '@/constants/enums'
import { usePropertyStore } from '@/stores/propertyStore'

const store = usePropertyStore()
const view = ref('卡片视图')
const filters = reactive<Record<string, string>>({})
const propertyTypes = Object.values(PropertyType)
const propertyStatuses = Object.values(PropertyStatus)
async function load() { await store.fetch(filters) }
onMounted(load)
</script>
