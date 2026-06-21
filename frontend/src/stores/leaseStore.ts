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
  },
})

