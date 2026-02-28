<template>
  <div class="contact-page">
    <!-- Hero -->
    <section class="bg-gradient-to-b from-gray-50 to-white pt-16 pb-12 md:pt-20 md:pb-16 border-b border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-semibold text-gray-900 mb-4 tracking-tight">
          Get in touch
        </h1>
        <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
          We're here to help and answer any questions you might have
        </p>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="py-16 md:py-20 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Contact Form -->
          <div class="border border-gray-200 rounded-lg p-6">
            <h2 class="text-2xl font-semibold text-gray-900 mb-5">Send us a message</h2>
            
            <!-- Success Message -->
            <div v-if="submitSuccess" class="text-center py-12">
              <div class="inline-flex items-center justify-center w-16 h-16 bg-green-100 text-green-600 rounded-full mb-4">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-2">Message Sent!</h3>
              <p class="text-gray-600 mb-6">{{ submitMessage }}</p>
              <button 
                @click="resetForm"
                class="btn-primary"
              >
                Send Another Message
              </button>
            </div>

            <!-- Contact Form -->
            <form v-else @submit.prevent="handleSubmit" novalidate class="space-y-5">
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700 mb-1.5">Name</label>
                <input 
                  type="text" 
                  id="name" 
                  v-model="form.name"
                  @blur="validateField('name')"
                  @input="validateField('name')"
                  required
                  class="w-full px-3 py-2 text-sm border rounded-md focus:ring-1 transition-all"
                  :class="errors.name ? 'border-red-500 focus:ring-red-500 focus:border-red-500' : 'border-gray-300 focus:ring-palm-500 focus:border-palm-500'"
                  placeholder="John Doe"
                >
                <p v-if="errors.name" class="mt-1 text-xs text-red-600">{{ errors.name }}</p>
              </div>
              
              <div>
                <label for="email" class="block text-sm font-medium text-gray-700 mb-1.5">Email</label>
                <input 
                  type="email" 
                  id="email" 
                  v-model="form.email"
                  @blur="validateField('email')"
                  @input="validateField('email')"
                  required
                  class="w-full px-3 py-2 text-sm border rounded-md focus:ring-1 transition-all"
                  :class="errors.email ? 'border-red-500 focus:ring-red-500 focus:border-red-500' : 'border-gray-300 focus:ring-palm-500 focus:border-palm-500'"
                  placeholder="your@email.com"
                >
                <p v-if="errors.email" class="mt-1 text-xs text-red-600">{{ errors.email }}</p>
              </div>
              
              <div>
                <label for="phone" class="block text-sm font-medium text-gray-700 mb-1.5">Phone</label>
                <input 
                  type="tel" 
                  id="phone" 
                  v-model="form.phone"
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-1 focus:ring-palm-500 focus:border-palm-500 transition-all"
                  placeholder="+230 5xxx xxxx"
                >
              </div>
              
              <div>
                <label for="subject" class="block text-sm font-medium text-gray-700 mb-1.5">Subject</label>
                <select 
                  id="subject" 
                  v-model="form.subject"
                  required
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-1 focus:ring-palm-500 focus:border-palm-500 transition-all"
                >
                  <option value="">Select a subject</option>
                  <option value="sales">Sales Inquiry</option>
                  <option value="support">Technical Support</option>
                  <option value="demo">Request Demo</option>
                  <option value="other">Other</option>
                </select>
              </div>
              
              <div>
                <label for="message" class="block text-sm font-medium text-gray-700 mb-1.5">Message</label>
                <textarea 
                  id="message" 
                  v-model="form.message"
                  @blur="validateField('message')"
                  @input="validateField('message')"
                  required
                  rows="4"
                  class="w-full px-3 py-2 text-sm border rounded-md focus:ring-1 transition-all"
                  :class="errors.message ? 'border-red-500 focus:ring-red-500 focus:border-red-500' : 'border-gray-300 focus:ring-palm-500 focus:border-palm-500'"
                  placeholder="How can we help you?"
                ></textarea>
                <p v-if="errors.message" class="mt-1 text-xs text-red-600">{{ errors.message }}</p>
              </div>
              
              <button 
                type="submit" 
                class="w-full btn-primary"
                :disabled="submitting"
              >
                {{ submitting ? 'Sending...' : 'Send message' }}
              </button>
              
              <p v-if="submitMessage && !submitSuccess" class="text-center text-sm text-red-600">
                {{ submitMessage }}
              </p>
            </form>
          </div>

          <!-- Contact Info -->
          <div class="space-y-6">
            <div class="border border-gray-200 rounded-lg p-6">
              <h3 class="text-xl font-semibold text-gray-900 mb-5">Contact information</h3>
              <div class="space-y-4">
                <div class="flex items-start gap-3">
                  <div class="flex-shrink-0 w-10 h-10 bg-gray-100 text-gray-700 rounded-md flex items-center justify-center">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-sm font-semibold text-gray-900 mb-0.5">Address</h4>
                    <p class="text-sm text-gray-600">Port Louis, Mauritius</p>
                  </div>
                </div>
                
                <div class="flex items-start gap-3">
                  <div class="flex-shrink-0 w-10 h-10 bg-gray-100 text-gray-700 rounded-md flex items-center justify-center">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-sm font-semibold text-gray-900 mb-0.5">Email</h4>
                    <a href="mailto:support@palmposmu.com" class="text-sm text-palm-600 hover:text-palm-700">support@palmposmu.com</a>
                  </div>
                </div>
              </div>
            </div>

            <div class="card bg-palm-50">
              <h3 class="text-2xl font-bold text-gray-900 mb-4">Business Hours</h3>
              <div class="space-y-2 text-gray-600">
                <div class="flex justify-between">
                  <span>Monday - Friday:</span>
                  <span class="font-medium">9:00 AM - 5:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span>Saturday:</span>
                  <span class="font-medium">9:00 AM - 1:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span>Sunday:</span>
                  <span class="font-medium">Closed</span>
                </div>
              </div>
            </div>

            <div class="card bg-gradient-to-br from-palm-600 to-primary-600 text-white">
              <h3 class="text-2xl font-bold mb-4">Need Immediate Help?</h3>
              <p class="mb-6">
                Try our demo to see PalmPOS in action or check our documentation for common questions.
              </p>
              <div class="flex gap-4">
                <router-link to="/demo"
                   class="px-6 py-3 bg-white text-palm-600 font-semibold rounded-lg hover:bg-gray-100 transition-colors">
                  Try Demo
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { API_ENDPOINTS } from '../config/api'

const form = ref({
  name: '',
  email: '',
  phone: '',
  subject: '',
  message: ''
})

const errors = ref({
  name: '',
  email: '',
  phone: '',
  subject: '',
  message: ''
})

const submitting = ref(false)
const submitMessage = ref('')
const submitSuccess = ref(false)

const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return re.test(email)
}

const validateField = (field) => {
  switch (field) {
    case 'name':
      if (!form.value.name.trim()) {
        errors.value.name = 'Name is required'
      } else {
        errors.value.name = ''
      }
      break
    case 'email':
      if (!form.value.email.trim()) {
        errors.value.email = 'Email is required'
      } else if (!validateEmail(form.value.email)) {
        errors.value.email = 'Please enter a valid email address'
      } else {
        errors.value.email = ''
      }
      break
    case 'message':
      if (!form.value.message.trim()) {
        errors.value.message = 'Message is required'
      } else {
        errors.value.message = ''
      }
      break
  }
}

const validateForm = () => {
  let isValid = true
  errors.value = {
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  }
  
  if (!form.value.name.trim()) {
    errors.value.name = 'Name is required'
    isValid = false
  }
  
  if (!form.value.email.trim()) {
    errors.value.email = 'Email is required'
    isValid = false
  } else if (!validateEmail(form.value.email)) {
    errors.value.email = 'Please enter a valid email address'
    isValid = false
  }
  
  if (!form.value.message.trim()) {
    errors.value.message = 'Message is required'
    isValid = false
  }
  
  return isValid
}

const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }
  submitting.value = true
  submitMessage.value = ''
  submitSuccess.value = false
  
  try {
    const response = await fetch(API_ENDPOINTS.CONTACT_SUBMIT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'call',
        params: form.value,
        id: Date.now()
      })
    })
    
    const data = await response.json()
    
    if (data.result && data.result.success) {
      submitSuccess.value = true
      submitMessage.value = data.result.message
    } else {
      submitSuccess.value = false
      submitMessage.value = data.result?.message || 'An error occurred. Please try again.'
    }
    
  } catch (error) {
    console.error('Form submission error:', error)
    submitSuccess.value = false
    submitMessage.value = 'An error occurred. Please try again or email us at support@palmposmu.com'
  } finally {
    submitting.value = false
  }
}

const resetForm = () => {
  form.value = {
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  }
  submitSuccess.value = false
  submitMessage.value = ''
  errors.value = {
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  }
}
</script>
