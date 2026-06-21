import { createRouter, createWebHistory } from 'vue-router'
import { UserRole } from '@/constants/enums'
import { setupGuards } from './guards'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('@/pages/Home.vue'), meta: { requiresAuth: true } },
    { path: '/login', component: () => import('@/pages/Login.vue') },
    { path: '/register', component: () => import('@/pages/Register.vue') },
    { path: '/properties', component: () => import('@/pages/PropertyList.vue') },
    { path: '/properties/new', component: () => import('@/pages/PropertyForm.vue'), meta: { requiresAuth: true, roles: [UserRole.LANDLORD] } },
    { path: '/properties/:id', component: () => import('@/pages/PropertyDetail.vue') },
    { path: '/properties/:id/edit', component: () => import('@/pages/PropertyForm.vue'), meta: { requiresAuth: true, roles: [UserRole.LANDLORD] } },
    { path: '/leases', component: () => import('@/pages/LeaseList.vue'), meta: { requiresAuth: true } },
    { path: '/leases/:id', component: () => import('@/pages/LeaseDetail.vue'), meta: { requiresAuth: true } },
    { path: '/bills', component: () => import('@/pages/BillCenter.vue'), meta: { requiresAuth: true } },
    { path: '/repairs', component: () => import('@/pages/RepairList.vue'), meta: { requiresAuth: true } },
    { path: '/repairs/new', component: () => import('@/pages/RepairForm.vue'), meta: { requiresAuth: true, roles: [UserRole.TENANT] } },
    { path: '/:pathMatch(.*)*', component: () => import('@/pages/NotFound.vue') },
  ],
})

setupGuards(router)
export default router

