import { defineStore } from 'pinia'
import { leaseApi } from '@/api/lease'
import type { Lease } from '@/types/lease'

export const useLeaseStore = defineStore('lease', {
  state: () => ({ items: [] as Lease[], current: null as Lease | null }),
  actions: {
    async fetch() {
      const data = await leaseApi.list()
      this.items = data.results
    },
    async fetchOne(id: string) {
      this.current = await leaseApi.detail(id)
    },
    async terminate(id: string, data: { terminationReason: string; penaltyAmount?: number | string }) {
      const result = await leaseApi.terminate(id, data)
      if (this.current?.id === id) {
        this.current = result
      }
      return result
    },
  },
})

