<template>
  <div class="pricing-page">
    <!-- Hero -->
    <section class="bg-gradient-to-b from-gray-50 to-white pt-16 pb-12 md:pt-20 md:pb-16 border-b border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-semibold text-gray-900 mb-4 tracking-tight">
          Simple, transparent pricing
        </h1>
        <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
          Choose the perfect plan for your business size and needs
        </p>
      </div>
    </section>

    <!-- Demo Notice -->
    <section class="py-6 bg-palm-50 border-b border-palm-100">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-start gap-3 text-center justify-center">
          <svg class="w-5 h-5 text-palm-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <div>
            <p class="text-sm text-gray-700">
              <strong>Not sure which plan is right for you?</strong> 
              <router-link to="/demo" class="text-palm-600 hover:text-palm-700 font-medium underline">Try our free demo</router-link> 
              to explore all features and see how PalmPOS works before making a decision.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Pricing Cards -->
    <section class="py-16 md:py-20 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(plan, index) in plans" :key="index" 
               class="bg-white rounded-lg border hover:shadow-md transition-all duration-200"
               :class="plan.popular ? 'border-palm-600 shadow-md' : 'border-gray-200'">
            <div v-if="plan.popular" class="bg-palm-600 text-white text-center py-2 text-sm font-medium">
              Most Popular
            </div>
            <div class="p-6">
              <h3 class="text-xl font-semibold text-gray-900 mb-1">{{ plan.name }}</h3>
              <p class="text-sm text-gray-600 mb-4">{{ plan.description }}</p>
              
              <div class="mb-1">
                <span class="text-4xl font-semibold text-gray-900">{{ plan.price }}</span>
                <span class="text-gray-600 text-sm" v-if="plan.price !== 'Contact Us'">/month</span>
              </div>
              
              <div v-if="plan.setupFee" class="mb-5 text-sm text-gray-500">
                + {{ plan.setupFee }} setup fee
              </div>
              <div v-else class="mb-5 text-sm text-gray-500">
                Custom setup pricing
              </div>
              
              <button 
                @click="openModal(plan)"
                class="w-full py-2.5 rounded-md text-sm font-medium transition-colors duration-150"
                :class="plan.popular ? 'bg-palm-600 text-white hover:bg-palm-700' : 'bg-gray-100 text-gray-900 hover:bg-gray-200'"
              >
                {{ plan.price === 'Contact Us' ? 'Contact sales' : 'Get started' }}
              </button>
              
              <ul class="mt-6 space-y-3">
                <li v-for="feature in plan.features" :key="feature" class="flex items-start gap-3">
                  <svg class="w-5 h-5 text-palm-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="text-sm text-gray-700">{{ feature }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="showModal" class="fixed inset-0 z-50 overflow-y-auto" @click.self="closeModal">
          <div class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
            <!-- Background overlay -->
            <div class="fixed inset-0 transition-opacity bg-gray-900 bg-opacity-75" @click="closeModal"></div>

            <!-- Modal panel -->
            <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
              <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                <div class="flex items-start justify-between mb-4">
                  <div>
                    <h3 class="text-2xl font-bold text-gray-900">
                      Get Started with {{ selectedPlan?.name }}
                    </h3>
                    <p class="mt-1 text-sm text-gray-500">
                      Fill in your details and we'll get back to you within 24 hours with more information about your selected plan.
                    </p>
                  </div>
                  <button @click="closeModal" class="text-gray-400 hover:text-gray-500">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>

                <form @submit.prevent="submitForm" class="space-y-4">
                  <div>
                    <label for="modal-name" class="block text-sm font-medium text-gray-700 mb-1">Full Name*</label>
                    <input 
                      type="text" 
                      id="modal-name"
                      v-model="formData.name"
                      required
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-palm-500 focus:border-transparent"
                      placeholder="John Doe"
                    >
                  </div>

                  <div>
                    <label for="modal-email" class="block text-sm font-medium text-gray-700 mb-1">Email*</label>
                    <input 
                      type="email" 
                      id="modal-email"
                      v-model="formData.email"
                      required
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-palm-500 focus:border-transparent"
                      placeholder="john@company.com"
                    >
                  </div>

                  <div>
                    <label for="modal-phone" class="block text-sm font-medium text-gray-700 mb-1">Phone*</label>
                    <input 
                      type="tel" 
                      id="modal-phone"
                      v-model="formData.phone"
                      required
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-palm-500 focus:border-transparent"
                      placeholder="+230 5xxx xxxx"
                    >
                  </div>

                  <div>
                    <label for="modal-company" class="block text-sm font-medium text-gray-700 mb-1">Company Name*</label>
                    <input 
                      type="text" 
                      id="modal-company"
                      v-model="formData.company"
                      required
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-palm-500 focus:border-transparent"
                      placeholder="Your Business Name"
                    >
                  </div>

                  <div>
                    <label for="modal-message" class="block text-sm font-medium text-gray-700 mb-1">Additional Information</label>
                    <textarea 
                      id="modal-message"
                      v-model="formData.message"
                      rows="3"
                      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-palm-500 focus:border-transparent"
                      placeholder="Any additional information you'd like to share..."
                    ></textarea>
                  </div>

                  <div class="bg-palm-50 p-4 rounded-lg">
                    <p class="text-sm text-gray-700">
                      <strong>Selected Plan:</strong> {{ selectedPlan?.name }}<br>
                      <strong>Price:</strong> {{ selectedPlan?.price }}<span v-if="selectedPlan?.price !== 'Contact Us'">/month</span><br>
                      <span v-if="selectedPlan?.setupFee">
                        <strong>Setup Fee:</strong> {{ selectedPlan?.setupFee }}
                      </span>
                    </p>
                  </div>

                  <div class="flex gap-3 pt-4">
                    <button 
                      type="button"
                      @click="closeModal"
                      class="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
                    >
                      Cancel
                    </button>
                    <button 
                      type="submit"
                      :disabled="submitting"
                      class="flex-1 px-4 py-2 bg-palm-600 text-white rounded-lg hover:bg-palm-700 transition-colors disabled:opacity-50"
                    >
                      {{ submitting ? 'Sending...' : 'Submit Request' }}
                    </button>
                  </div>

                  <p v-if="submitMessage" 
                     class="text-center text-sm"
                     :class="submitSuccess ? 'text-palm-600' : 'text-red-600'">
                    {{ submitMessage }}
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- FAQ -->
    <section class="py-20 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold text-center text-gray-900 mb-12">Frequently Asked Questions</h2>
        <div class="space-y-6">
          <div v-for="(faq, index) in faqs" :key="index" class="card">
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ faq.question }}</h3>
            <p class="text-gray-600">{{ faq.answer }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const plans = [
  {
    name: 'Starter',
    description: 'Small Business',
    price: 'Rs 1,500',
    setupFee: 'Free',
    popular: false,
    features: [
      '1 POS terminal & 1 warehouse',
      'Up to 2 concurrent users',
      'Web & mobile-friendly POS interface',
      'Product catalog management',
      'Barcode scanning',
      'Cash & card payment processing',
      'Daily sales & cash flow reports',
      'Customer orders & invoicing',
      'Email receipts',
      'Basic inventory tracking',
      'Product variants (size, color, etc.)',
      'Purchase orders & supplier management',
      'Cloud-based data storage & secure backups',
      'Email support (48h response)',
    ]
  },
  {
    name: 'Professional',
    description: 'Growing Business',
    price: 'Rs 5,000',
    setupFee: 'Rs 25,000',
    popular: true,
    features: [
      'Up to 3 POS terminals & 2 warehouses',
      'Up to 10 concurrent users',
      'Handheld terminal for POS (rented) included',
      'Online availability & cloud access everywhere',
      'Barcode scanner included',
      'Receipt printer included',
      'Customer display screen included',
      'Multi-warehouse inventory management & syncing',
      'Basic discount management across devices',
      'Employee shifts & permissions',
      'Offline mode capability',
      'Priority support (24h response)',
      'Cloud-based data storage & secure backups',
      'Hardware security recommendations',
    ]
  },
  {
    name: 'Enterprise',
    description: 'Multi-location Business',
    price: 'Contact Us',
    setupFee: null,
    popular: false,
    features: [
      'Unlimited POS terminals & warehouses',
      'Unlimited users',
      'Full POS terminals or handheld devices available',
      'Custom hardware setup tailored to your needs',
      'Multi-company / multi-location management',
      'Accounting & financial reports',
      'Cloud-based storage with daily backups',
      'Full online & offline access anywhere',
      'Enhanced hardware security & device management',
      'API access for custom integrations',
      'Custom workflows & add-ons tailored to business needs',
      'Dedicated account manager & optional on-site training',
      '24/7 priority support',
    ]
  },
]

const faqs = [
  {
    question: 'Can I change plans later?',
    answer: 'Yes, you can upgrade or downgrade your plan at any time. Changes will be reflected in your next billing cycle.'
  },
  {
    question: 'What does the setup fee cover?',
    answer: 'The Starter plan includes free setup for web-only access. Professional plan setup includes handheld terminal rental, hardware installation, system configuration, data migration, training sessions, and onboarding support. Enterprise plans include custom hardware setups (full terminals or handheld devices) tailored to your specific business needs.'
  },
  {
    question: 'What payment methods do you accept?',
    answer: 'We accept all major credit cards, bank transfers, and local payment methods in Mauritius.'
  },
  {
    question: 'Is there a free trial?',
    answer: 'Yes, we offer a 14-day free trial with the demo system. For custom solutions, we can arrange a personalized demo.'
  },
  {
    question: 'What happens to my data if I cancel?',
    answer: 'You can export all your data at any time. We keep your data for 30 days after cancellation in case you change your mind.'
  },
  {
    question: 'Do you provide training?',
    answer: 'Yes! Basic training is included with Professional plan setup, and comprehensive on-site training is available with Enterprise plans. All plans also include access to our documentation and support resources.'
  },
]

const showModal = ref(false)
const selectedPlan = ref(null)
const submitting = ref(false)
const submitMessage = ref('')
const submitSuccess = ref(false)

const formData = ref({
  name: '',
  email: '',
  phone: '',
  company: '',
  message: ''
})

const openModal = (plan) => {
  selectedPlan.value = plan
  showModal.value = true
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  showModal.value = false
  selectedPlan.value = null
  submitMessage.value = ''
  document.body.style.overflow = ''
}

const submitForm = async () => {
  submitting.value = true
  submitMessage.value = ''
  
  // Simulate form submission
  // In production, this would send to your backend API
  setTimeout(() => {
    submitting.value = false
    submitSuccess.value = true
    submitMessage.value = 'Thank you! We\'ve received your request and will contact you within 24 hours.'
    
    // Log the data (in production, this would be sent to backend)
    console.log('Plan Request:', {
      plan: selectedPlan.value.name,
      planPrice: selectedPlan.value.price,
      setupFee: selectedPlan.value.setupFee,
      ...formData.value,
      timestamp: new Date().toISOString()
    })
    
    // Reset form after showing success message
    setTimeout(() => {
      formData.value = {
        name: '',
        email: '',
        phone: '',
        company: '',
        message: ''
      }
      closeModal()
    }, 3000)
  }, 1000)
}
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .inline-block,
.modal-leave-active .inline-block {
  transition: transform 0.3s ease;
}

.modal-enter-from .inline-block,
.modal-leave-to .inline-block {
  transform: scale(0.95);
}
</style>
