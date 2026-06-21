<template>
  <article class="property-card" @click="$router.push(`/properties/${property.id}`)">
    <img :src="cover" :alt="property.title" />
    <div class="property-card__body">
      <div class="property-card__top">
        <el-tag>{{ enumLabels[property.type] }}</el-tag>
        <StatusBadge :value="property.status" domain="property" />
      </div>
      <h3>{{ property.title }}</h3>
      <p>{{ property.rooms }} · {{ property.area }}㎡ · {{ property.floor }}/{{ property.totalFloors }}层</p>
      <strong>{{ formatMoney(property.price) }}/月</strong>
    </div>
  </article>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import StatusBadge from './StatusBadge.vue'
import { enumLabels } from '@/constants/enums'
import type { Property } from '@/types/property'
import { formatMoney } from '@/utils/format'

const props = defineProps<{ property: Property }>()
const cover = computed(() => props.property.images?.[0] || 'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d')
</script>
