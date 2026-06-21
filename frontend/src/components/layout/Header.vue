<template>
  <header class="app-header">
    <div>
      <strong>RentHub</strong>
      <span>租赁全流程运营台</span>
    </div>
    <div class="header-actions">
      <el-tag v-if="auth.user">{{ enumLabels[auth.user.role] }} · {{ auth.user.nickname || auth.user.username }}</el-tag>
      <el-button v-if="auth.isLoggedIn" text @click="logout">退出</el-button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { enumLabels } from '@/constants/enums'
import { useAuthStore } from '@/stores/authStore'

const auth = useAuthStore()
const router = useRouter()
function logout() {
  auth.logout()
  router.push('/login')
}
</script>

