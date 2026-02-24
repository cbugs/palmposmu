<template>
  <div class="features-page">
    <!-- Hero -->
    <section class="bg-gradient-to-b from-gray-50 to-white pt-16 pb-12 md:pt-20 md:pb-16 border-b border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-semibold text-gray-900 mb-4 tracking-tight">
          Powerful features for your business
        </h1>
        <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
          Everything you need to streamline operations and accelerate growth
        </p>
      </div>
    </section>

    <!-- Detailed Features -->
    <section class="py-16 md:py-20 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div v-for="(category, index) in featureCategories" :key="index" class="mb-16 last:mb-0">
          <div class="text-center mb-10 max-w-2xl mx-auto">
            <h2 class="text-2xl md:text-3xl font-semibold text-gray-900 mb-2 tracking-tight">{{ category.title }}</h2>
            <p class="text-base text-gray-600">{{ category.description }}</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div v-for="feature in category.features" :key="feature.name" 
                 class="flex gap-4 p-5 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
              <div class="flex-shrink-0 text-palm-600 mt-0.5">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <div>
                <h3 class="text-base font-semibold text-gray-900 mb-1">{{ feature.name }}</h3>
                <p class="text-sm text-gray-600 leading-relaxed">{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Integration Section -->
    <section class="py-16 bg-gray-50 border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-10 max-w-2xl mx-auto">
          <h2 class="text-2xl md:text-3xl font-semibold text-gray-900 mb-2 tracking-tight">Seamless integrations</h2>
          <p class="text-base text-gray-600">Connect with the tools you already use</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div v-for="integration in integrations" :key="integration" 
               class="p-5 bg-white rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200 text-center">
            <div class="text-sm font-medium text-gray-900">{{ integration }}</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const featureCategories = [
  {
    title: 'Sales & Point of Sale',
    description: 'Fast and intuitive sales processing',
    features: [
      { name: 'Quick Sale Processing', description: 'Lightning-fast checkout with barcode scanning and touch-friendly interface' },
      { name: 'Multiple Payment Methods', description: 'Accept cash, cards, mobile payments, and split payments' },
      { name: 'Offline Mode', description: 'Continue selling even without internet connection' },
      { name: 'Receipt Customization', description: 'Create branded receipts with your logo and custom messages' },
      { name: 'Returns & Refunds', description: 'Handle returns and refunds with full audit trail' },
      { name: 'Discounts & Promotions', description: 'Apply automatic discounts, coupons, and promotional offers' },
    ]
  },
  {
    title: 'Inventory Management',
    description: 'Complete control over your stock',
    features: [
      { name: 'Real-Time Stock Tracking', description: 'Monitor inventory levels across all locations in real-time' },
      { name: 'Automated Reordering', description: 'Set reorder points and automate purchase orders' },
      { name: 'Lot & Serial Number Tracking', description: 'Track products by lot numbers and serial numbers' },
      { name: 'Multi-Warehouse Support', description: 'Manage inventory across multiple warehouses and stores' },
      { name: 'Stock Adjustments', description: 'Easy inventory adjustments with full history tracking' },
      { name: 'Product Variants', description: 'Manage products with multiple sizes, colors, and attributes' },
    ]
  },
  {
    title: 'Customer Management',
    description: 'Build lasting customer relationships',
    features: [
      { name: 'Customer Profiles', description: 'Detailed customer information and purchase history' },
      { name: 'Loyalty Programs', description: 'Reward repeat customers with points and rewards' },
      { name: 'Gift Cards', description: 'Sell and redeem gift cards easily' },
      { name: 'Customer Groups', description: 'Segment customers for targeted marketing' },
      { name: 'Credit Management', description: 'Manage customer credit and payment terms' },
      { name: 'Marketing Tools', description: 'Send targeted emails and SMS campaigns' },
    ]
  },
  {
    title: 'Reporting & Analytics',
    description: 'Make data-driven decisions',
    features: [
      { name: 'Sales Reports', description: 'Detailed sales analysis by product, category, time, and staff' },
      { name: 'Inventory Reports', description: 'Stock levels, movements, and valuation reports' },
      { name: 'Financial Reports', description: 'Profit/loss, cash flow, and tax reports' },
      { name: 'Custom Dashboards', description: 'Create personalized dashboards with key metrics' },
      { name: 'Export Data', description: 'Export reports to Excel, PDF, and other formats' },
      { name: 'Scheduled Reports', description: 'Automatically email reports on a schedule' },
    ]
  },
  {
    title: 'Employee Management',
    description: 'Manage your team effectively',
    features: [
      { name: 'User Roles & Permissions', description: 'Control access with granular permission settings' },
      { name: 'Time Clock', description: 'Track employee hours and attendance' },
      { name: 'Sales by Employee', description: 'Monitor individual employee performance' },
      { name: 'Commission Tracking', description: 'Calculate and track sales commissions' },
      { name: 'Activity Logs', description: 'Complete audit trail of all user actions' },
      { name: 'Multi-User Support', description: 'Unlimited users with concurrent access' },
    ]
  },
  {
    title: 'E-Commerce & Omnichannel',
    description: 'Unify online and offline sales',
    features: [
      { name: 'Online Store Integration', description: 'Sync inventory and orders with your online store' },
      { name: 'Click & Collect', description: 'Enable buy online, pick up in store' },
      { name: 'Unified Inventory', description: 'Single inventory across all channels' },
      { name: 'Order Management', description: 'Manage orders from all channels in one place' },
      { name: 'Customer Sync', description: 'Unified customer data across channels' },
      { name: 'Marketplace Integration', description: 'Connect with major marketplaces' },
    ]
  },
]

const integrations = [
  'Accounting Software',
  'E-Commerce Platforms',
  'Payment Gateways',
  'Shipping Providers',
  'Email Marketing',
  'SMS Services',
  'Barcode Scanners',
  'Receipt Printers',
]
</script>
