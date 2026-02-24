<template>
  <nav class="bg-white border-b border-gray-200 sticky top-0 z-50 backdrop-blur-sm bg-white/95">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-2 group">
          <img src="/palmpos.png" alt="PalmPOS" class="h-7 w-7 transition-transform group-hover:scale-105">
          <span class="text-lg font-semibold text-gray-900">PalmPOS</span>
        </router-link>

        <!-- Desktop Menu -->
        <div class="hidden md:flex items-center space-x-1">
          <router-link 
            v-for="item in menuItems" 
            :key="item.path"
            :to="item.path"
            class="text-sm text-gray-600 hover:text-gray-900 transition-colors duration-150 px-3 py-2 rounded-md hover:bg-gray-50"
            active-class="text-gray-900 bg-gray-50"
          >
            {{ item.name }}
          </router-link>
          <router-link
            to="/demo"
            class="btn-primary ml-4"
          >
            Demo
          </router-link>
        </div>

        <!-- Mobile menu button -->
        <button 
          @click="mobileMenuOpen = !mobileMenuOpen" 
          class="md:hidden text-gray-700 hover:text-palm-600 focus:outline-none"
        >
          <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path 
              v-if="!mobileMenuOpen" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path 
              v-else 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="slide-down">
      <div v-if="mobileMenuOpen" class="md:hidden bg-white border-t border-gray-200">
        <div class="px-4 py-3 space-y-1">
          <router-link 
            v-for="item in menuItems" 
            :key="item.path"
            :to="item.path"
            @click="mobileMenuOpen = false"
            class="block px-3 py-2 rounded-md text-sm text-gray-700 hover:text-gray-900 hover:bg-gray-50 transition-colors duration-150"
            active-class="text-gray-900 bg-gray-50"
          >
            {{ item.name }}
          </router-link>
          <router-link
            to="/demo"
            @click="mobileMenuOpen = false"
            class="block px-3 py-2 rounded-md text-sm font-medium text-palm-600 hover:bg-gray-50 transition-colors duration-150"
          >
            Demo
          </router-link>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'

const mobileMenuOpen = ref(false)
const scrolled = ref(false)

const menuItems = [
  { name: 'Home', path: '/' },
  { name: 'Features', path: '/features' },
  { name: 'Pricing', path: '/pricing' },
  { name: 'About', path: '/about' },
  { name: 'Contact', path: '/contact' },
]

const handleScroll = () => {
  scrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.slide-down-leave-to {
  opacity: 0;
}
</style>
