<template>
  <div class="auth-page">
    <el-card class="auth-panel">
      <h1>注册 RentHub</h1>
      <el-form :model="form" label-position="top">
        <el-form-item label="用户名"><el-input v-model="form.username" /></el-form-item>
        <el-form-item label="密码"><el-input v-model="form.password" type="password" /></el-form-item>
        <el-form-item label="角色">
          <el-segmented v-model="form.role" :options="roleOptions" />
        </el-form-item>
        <el-form-item label="昵称"><el-input v-model="form.nickname" /></el-form-item>
        <el-form-item label="手机号"><el-input v-model="form.phone" /></el-form-item>
        <el-button type="primary" class="full" @click="submit">注册</el-button>
      </el-form>
      <router-link to="/login">已有账号，去登录</router-link>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { authApi } from '@/api/auth'
import { UserRole } from '@/constants/enums'

const router = useRouter()
const roleOptions = [{ label: '房东', value: UserRole.LANDLORD }, { label: '租客', value: UserRole.TENANT }]
const form = reactive({ username: '', password: '', role: UserRole.TENANT, nickname: '', phone: '' })
async function submit() {
  await authApi.register(form)
  ElMessage.success('注册成功')
  router.push('/login')
}
</script>

