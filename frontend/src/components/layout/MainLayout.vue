<template>
  <div class="shell">
    <Sidebar />
    <main class="main">
      <Header />
      <section class="page-surface">
        <slot />
      </section>
      <Footer />
    </main>
  </div>
</template>

<script setup lang="ts">
import Header from './Header.vue'
import Sidebar from './Sidebar.vue'
import Footer from './Footer.vue'
</script>

