import { defineStore } from 'pinia'
import { propertyApi } from '@/api/property'
import type { Property } from '@/types/property'

export const usePropertyStore = defineStore('property', {
  state: () => ({ items: [] as Property[], current: null as Property | null }),
  actions: {
    async fetch(params?: Record<string, unknown>) {
      const data = await propertyApi.list(params)
      this.items = data.results
    },
    async fetchOne(id: string) {
      this.current = await propertyApi.detail(id)
    },
  },
})

