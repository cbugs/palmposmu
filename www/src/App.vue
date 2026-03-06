<template>
  <div id="app" class="min-h-screen flex flex-col">
    <Navbar v-if="!isUserGuidePage" />
    <main class="flex-grow">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <Footer v-if="!isUserGuidePage" />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';

const route = useRoute();
const isUserGuidePage = computed(() => route.path === '/user-guide');
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
