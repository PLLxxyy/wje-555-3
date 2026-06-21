import { computed } from 'vue'
import { UserRole } from '@/constants/enums'
import { useAuthStore } from '@/stores/authStore'

export function usePermission() {
  const auth = useAuthStore()
  const isLandlord = computed(() => auth.user?.role === UserRole.LANDLORD)
  const isTenant = computed(() => auth.user?.role === UserRole.TENANT)
  const isAdmin = computed(() => auth.user?.role === UserRole.ADMIN)
  return { isLandlord, isTenant, isAdmin }
}

