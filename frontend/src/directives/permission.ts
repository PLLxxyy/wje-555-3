import type { App, DirectiveBinding } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import type { UserRole } from '@/constants/enums'

function canUse(roles: UserRole[], role?: UserRole) {
  return Boolean(role && roles.includes(role))
}

export default {
  install(app: App) {
    app.directive('permission', {
      mounted(el: HTMLElement, binding: DirectiveBinding<UserRole[]>) {
        const auth = useAuthStore()
        if (!canUse(binding.value, auth.user?.role)) {
          el.remove()
        }
      },
    })
  },
}

