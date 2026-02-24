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
            <form @submit.prevent="handleSubmit" class="space-y-5">
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700 mb-1.5">Name</label>
                <input 
                  type="text" 
                  id="name" 
                  v-model="form.name"
                  required
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-1 focus:ring-palm-500 focus:border-palm-500 transition-all"
                  placeholder="Your name"
                >
              </div>
              
              <div>
                <label for="email" class="block text-sm font-medium text-gray-700 mb-1.5">Email</label>
                <input 
                  type="email" 
                  id="email" 
                  v-model="form.email"
                  required
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-1 focus:ring-palm-500 focus:border-palm-500 transition-all"
                  placeholder="your@email.com"
                >
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
                  required
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-1 focus:ring-palm-500 focus:border-palm-500 transition-all"
                  placeholder="How can we help you?"
                ></textarea>
              </div>
              
              <button 
                type="submit" 
                class="w-full btn-primary"
                :disabled="submitting"
              >
                {{ submitting ? 'Sending...' : 'Send message' }}
              </button>
              
              <p v-if="submitMessage" class="text-center text-sm" :class="submitSuccess ? 'text-palm-600' : 'text-red-600'">
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
                    <a href="mailto:info@palmpos.mu" class="text-sm text-palm-600 hover:text-palm-700">info@palmpos.mu</a>
                  </div>
                </div>
                
                <div class="flex items-start gap-3">
                  <div class="flex-shrink-0 w-10 h-10 bg-gray-100 text-gray-700 rounded-md flex items-center justify-center">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-sm font-semibold text-gray-900 mb-0.5">Phone</h4>
                    <a href="tel:+2305xxxxxxx" class="text-sm text-palm-600 hover:text-palm-700">+230 5xxx xxxx</a>
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

const form = ref({
  name: '',
  email: '',
  phone: '',
  subject: '',
  message: ''
})

const submitting = ref(false)
const submitMessage = ref('')
const submitSuccess = ref(false)

const handleSubmit = () => {
  submitting.value = true
  submitMessage.value = ''
  
  // Simulate form submission
  setTimeout(() => {
    submitting.value = false
    submitSuccess.value = true
    submitMessage.value = 'Thank you for your message! We\'ll get back to you shortly.'
    
    // Reset form
    form.value = {
      name: '',
      email: '',
      phone: '',
      subject: '',
      message: ''
    }
    
    // Clear message after 5 seconds
    setTimeout(() => {
      submitMessage.value = ''
    }, 5000)
  }, 1000)
}
</script>
