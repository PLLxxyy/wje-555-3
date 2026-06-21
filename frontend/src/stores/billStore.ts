import { defineStore } from 'pinia'
import { billApi } from '@/api/bill'
import type { Bill } from '@/types/bill'

export const useBillStore = defineStore('bill', {
  state: () => ({ items: [] as Bill[], stats: { pendingTotal: 0, paidTotal: 0, overdueTotal: 0 } }),
  actions: {
    async fetch(params?: Record<string, unknown>) {
      const data = await billApi.list(params)
      this.items = data.results
    },
    async fetchStats() {
      this.stats = await billApi.stats()
    },
  },
})

