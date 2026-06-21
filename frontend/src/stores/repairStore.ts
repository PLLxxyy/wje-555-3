import { defineStore } from 'pinia'
import { repairApi } from '@/api/repair'
import type { RepairOrder } from '@/types/repair'

export const useRepairStore = defineStore('repair', {
  state: () => ({ items: [] as RepairOrder[] }),
  actions: {
    async fetch() {
      const data = await repairApi.list()
      this.items = data.results
    },
  },
})

