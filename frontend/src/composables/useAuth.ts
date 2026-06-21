import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/authStore'

export function useAuth() {
  const auth = useAuthStore()
  return { auth, ...storeToRefs(auth) }
}

