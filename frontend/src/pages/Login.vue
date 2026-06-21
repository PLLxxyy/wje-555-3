<template>
  <div class="auth-page">
    <el-card class="auth-panel">
      <h1>RentHub</h1>
      <p>登录租赁管理平台</p>
      <el-form :model="form" label-position="top" @submit.prevent>
        <el-form-item label="用户名"><el-input v-model="form.username" /></el-form-item>
        <el-form-item label="密码"><el-input v-model="form.password" type="password" show-password /></el-form-item>
        <el-button type="primary" class="full" @click="submit">登录</el-button>
      </el-form>
      <router-link to="/register">创建房东或租客账号</router-link>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const form = reactive({ username: 'landlord', password: 'renthub123' })
const auth = useAuthStore()
const router = useRouter()
async function submit() {
  await auth.login(form.username, form.password)
  router.push('/')
}
</script>

