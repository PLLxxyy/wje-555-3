import type { Router } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import type { UserRole } from '@/constants/enums'

export function setupGuards(router: Router) {
  router.beforeEach(async (to) => {
    const auth = useAuthStore()
    if (auth.token && !auth.user) {
      await auth.loadProfile().catch(() => auth.logout())
    }
    if (to.meta.requiresAuth && !auth.isLoggedIn) return '/login'
    const roles = to.meta.roles as UserRole[] | undefined
    if (roles?.length && auth.user && !roles.includes(auth.user.role)) return '/'
    return true
  })
}

