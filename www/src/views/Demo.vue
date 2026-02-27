<template>
  <div class="demo-page">
    <!-- Hero -->
    <section class="bg-gradient-to-br from-palm-600 to-primary-600 text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl md:text-6xl font-bold mb-6 animate-slide-down">
          Try PalmPOS Demo
        </h1>
        <p class="text-xl md:text-2xl text-palm-50 max-w-3xl mx-auto">
          Experience the full power of PalmPOS with our interactive demo
        </p>
      </div>
    </section>

    <!-- Demo Instructions -->
    <section class="py-20 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="card bg-gradient-to-br from-palm-50 to-primary-50 mb-12">
          <div class="text-center mb-8">
            <div class="inline-flex items-center justify-center w-20 h-20 bg-palm-600 text-white rounded-full mb-4">
              <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h2 class="text-3xl font-bold text-gray-900 mb-4">Demo Credentials</h2>
            <p class="text-lg text-gray-600 mb-8">
              Use these credentials to log in and explore all features
            </p>
          </div>

          <div class="bg-white rounded-lg p-8 shadow-lg max-w-md mx-auto">
            <div class="space-y-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                <div class="flex items-center justify-between bg-gray-50 border border-gray-200 rounded-lg px-4 py-3">
                  <code class="text-lg font-mono text-gray-900">demo</code>
                  <button 
                    @click="copyToClipboard('demo')"
                    class="text-palm-600 hover:text-palm-700 transition-colors"
                    title="Copy to clipboard"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                  </button>
                </div>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                <div class="flex items-center justify-between bg-gray-50 border border-gray-200 rounded-lg px-4 py-3">
                  <code class="text-lg font-mono text-gray-900">password</code>
                  <button 
                    @click="copyToClipboard('password')"
                    class="text-palm-600 hover:text-palm-700 transition-colors"
                    title="Copy to clipboard"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            <div v-if="copyMessage" class="mt-4 text-center text-sm text-palm-600 animate-fade-in">
              {{ copyMessage }}
            </div>

            <div class="mt-8">
              <a 
                href="https://demo.palmposmu.com/" 
                target="_blank"
                rel="noopener noreferrer"
                class="block w-full bg-palm-600 text-white text-center font-bold py-4 px-6 rounded-lg hover:bg-palm-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl"
              >
                Launch Demo
                <svg class="inline-block w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        </div>

        <!-- What to Explore -->
        <div class="mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-8 text-center">What You Can Explore</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="card">
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-12 h-12 bg-palm-100 text-palm-600 rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>
                <div>
                  <h3 class="font-bold text-lg text-gray-900 mb-2">Point of Sale</h3>
                  <p class="text-gray-600">Process sales, manage cash registers, and handle customer transactions</p>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-12 h-12 bg-palm-100 text-palm-600 rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                  </svg>
                </div>
                <div>
                  <h3 class="font-bold text-lg text-gray-900 mb-2">Inventory Management</h3>
                  <p class="text-gray-600">Track stock levels, manage products, and handle warehouses</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Important Notes -->
        <div class="card bg-yellow-50 border-l-4 border-yellow-400">
          <div class="flex items-start gap-4">
            <div class="flex-shrink-0">
              <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-lg text-gray-900 mb-2">Important Notes</h3>
              <ul class="space-y-2 text-gray-700">
                <li class="flex items-start gap-2">
                  <svg class="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                  This is a shared demo environment - data may be reset periodically
                </li>
                <li class="flex items-start gap-2">
                  <svg class="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                  Feel free to explore all features - you can't break anything!
                </li>
                <li class="flex items-start gap-2">
                  <svg class="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                  For a personalized demo with your data, <router-link to="/contact" class="text-palm-600 hover:text-palm-700 font-semibold">contact our team</router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- CTA -->
        <div class="text-center mt-12">
          <p class="text-lg text-gray-600 mb-6">
            Have questions while exploring?
          </p>
          <router-link to="/contact" class="btn-secondary inline-block">
            Get Help from Our Team
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const copyMessage = ref('')

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
    copyMessage.value = '✓ Copied to clipboard!'
    setTimeout(() => {
      copyMessage.value = ''
    }, 2000)
  } catch (err) {
    copyMessage.value = 'Failed to copy'
    setTimeout(() => {
      copyMessage.value = ''
    }, 2000)
  }
}
</script>
