<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="relative bg-gradient-to-b from-gray-50 to-white pt-16 pb-20 md:pt-20 md:pb-24">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center">
          <h1 class="text-5xl md:text-6xl font-semibold text-gray-900 mb-5 tracking-tight leading-tight">
            Modern point of sale for Mauritius businesses
          </h1>
          <p class="text-lg md:text-xl text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
            Complete POS system for retail stores, restaurants, and cafes across Mauritius. Accept payments, manage inventory, and grow your business.
          </p>
          <div class="flex flex-col sm:flex-row gap-3 justify-center items-center">
            <router-link to="/pricing" class="btn-primary">
              Get started
            </router-link>
            <router-link to="/demo" class="btn-secondary">
              Try demo
            </router-link>
            <router-link to="/contact" class="btn-secondary">
              Contact sales
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Overview -->
    <section class="py-16 md:py-20 bg-white border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12 max-w-2xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-semibold text-gray-900 mb-3 tracking-tight">
            Everything you need to run your business
          </h2>
          <p class="text-lg text-gray-600 leading-relaxed">
            A complete suite of tools to manage sales, inventory, and customers
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(feature, index) in features" :key="index" 
               class="p-6 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
            <div class="text-palm-600 mb-3">
              <component :is="feature.icon" class="w-10 h-10" />
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ feature.title }}</h3>
            <p class="text-sm text-gray-600 leading-relaxed">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Cloud & Security Features -->
    <section class="py-16 md:py-20 bg-white border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12 max-w-2xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-semibold text-gray-900 mb-3 tracking-tight">
            Cloud-based and secure
          </h2>
          <p class="text-lg text-gray-600 leading-relaxed">
            Access your business from anywhere, on any device, with bank-level security
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          <div class="text-center">
            <div class="inline-flex items-center justify-center w-14 h-14 bg-palm-100 text-palm-600 rounded-xl mb-4">
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">100% Cloud-Based</h3>
            <p class="text-gray-600 leading-relaxed">
              No servers to install or maintain. Your data is securely stored in the cloud with automatic backups and updates.
            </p>
          </div>

          <div class="text-center">
            <div class="inline-flex items-center justify-center w-14 h-14 bg-palm-100 text-palm-600 rounded-xl mb-4">
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Enterprise Security</h3>
            <p class="text-gray-600 leading-relaxed">
              SSL encryption, secure data centers, regular security audits, and role-based access control protect your business 24/7.
            </p>
          </div>

          <div class="text-center">
            <div class="inline-flex items-center justify-center w-14 h-14 bg-palm-100 text-palm-600 rounded-xl mb-4">
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Access Anywhere</h3>
            <p class="text-gray-600 leading-relaxed">
              Works seamlessly on desktop, tablet, and mobile devices. Run your business from anywhere with internet access.
            </p>
          </div>
        </div>

        <div class="bg-gray-50 rounded-xl p-8 border border-gray-200">
          <div class="flex flex-wrap justify-center items-center gap-8 md:gap-12">
            <div class="flex items-center gap-3">
              <svg class="w-6 h-6 text-palm-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span class="text-sm font-medium text-gray-900">Desktop</span>
            </div>
            <div class="flex items-center gap-3">
              <svg class="w-6 h-6 text-palm-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
              <span class="text-sm font-medium text-gray-900">Tablet</span>
            </div>
            <div class="flex items-center gap-3">
              <svg class="w-6 h-6 text-palm-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
              <span class="text-sm font-medium text-gray-900">Mobile</span>
            </div>
            <div class="flex items-center gap-3">
              <svg class="w-6 h-6 text-palm-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
              <span class="text-sm font-medium text-gray-900">Offline Mode</span>
            </div>
            <div class="flex items-center gap-3">
              <svg class="w-6 h-6 text-palm-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              <span class="text-sm font-medium text-gray-900">Auto Sync</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="py-16 bg-gray-50 border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div v-for="stat in stats" :key="stat.label">
            <div class="text-3xl md:text-4xl font-semibold text-gray-900 mb-1">{{ stat.value }}</div>
            <div class="text-sm text-gray-600">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 md:py-20 bg-white border-t border-gray-100">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-semibold text-gray-900 mb-4 tracking-tight">
          Ready to get started?
        </h2>
        <p class="text-lg text-gray-600 mb-8 leading-relaxed">
          Join hundreds of businesses in Mauritius using PalmPOS
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center">
          <router-link to="/demo" class="btn-primary">
            Try demo
          </router-link>
          <router-link to="/contact" class="btn-secondary">
            Contact sales
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { h } from 'vue';

const features = [
  {
    title: 'Sales Management',
    description: 'Process transactions quickly with an intuitive interface designed for speed and efficiency.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z' })
    ])
  },
  {
    title: 'Inventory Control',
    description: 'Track stock levels in real-time, manage suppliers, and automate reordering.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4' })
    ])
  },
  {
    title: 'Customer Management',
    description: 'Build lasting relationships with integrated CRM and loyalty programs.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' })
    ])
  },
  {
    title: 'Financial Reporting',
    description: 'Comprehensive analytics and reports to track your business performance.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' })
    ])
  },
  {
    title: 'Multi-Location Support',
    description: 'Manage multiple stores from a single dashboard with centralized control.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z' }),
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M15 11a3 3 0 11-6 0 3 3 0 016 0z' })
    ])
  },
  {
    title: 'E-Commerce Integration',
    description: 'Seamlessly connect your online and offline sales channels.',
    icon: () => h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9' })
    ])
  },
]

const stats = [
  { value: '500+', label: 'Active Businesses' },
  { value: '1M+', label: 'Transactions/Month' },
  { value: '99.9%', label: 'Uptime' },
  { value: '24/7', label: 'Support' },
]
</script>
