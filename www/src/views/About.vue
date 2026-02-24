<template>
  <div class="about-page">
    <!-- Hero -->
    <section class="bg-gradient-to-b from-gray-50 to-white pt-16 pb-12 md:pt-20 md:pb-16 border-b border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-semibold text-gray-900 mb-4 tracking-tight">
          About Palmtree Mauritius
        </h1>
        <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
          Empowering businesses across Mauritius with innovative technology
        </p>
      </div>
    </section>

    <!-- Story Section -->
    <section class="py-16 md:py-20 bg-white">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl md:text-3xl font-semibold text-gray-900 mb-5 tracking-tight">Our story</h2>
        <div class="text-base text-gray-600 space-y-4 leading-relaxed">
          <p>
            Founded in Mauritius, Palmtree is dedicated to helping local businesses thrive in the digital age. 
            We recognized that many businesses were struggling with outdated, complex systems that held them back 
            rather than helping them grow.
          </p>
          <p>
            That's why we created PalmPOS - a modern, intuitive point of sale system designed specifically for 
            the needs of Mauritian businesses. Whether you run a retail store, restaurant, or service business, 
            PalmPOS provides the tools you need to succeed.
          </p>
          <p>
            Today, we're proud to serve hundreds of businesses across Mauritius, processing millions of 
            transactions and helping our clients grow their revenue and improve their operations.
          </p>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="py-16 bg-gray-50 border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl md:text-3xl font-semibold text-center text-gray-900 mb-10 tracking-tight">Our values</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="value in values" :key="value.title" class="p-6 bg-white rounded-lg border border-gray-200 text-center hover:border-gray-300 hover:shadow-sm transition-all duration-200">
            <div class="text-4xl mb-3">{{ value.icon }}</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ value.title }}</h3>
            <p class="text-sm text-gray-600 leading-relaxed">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="py-16 md:py-20 bg-white border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl md:text-3xl font-semibold text-center text-gray-900 mb-10 tracking-tight">Our commitment</h2>
        <div class="max-w-4xl mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-5 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
              <h3 class="text-base font-semibold text-gray-900 mb-2">🎯 Customer success</h3>
              <p class="text-sm text-gray-600 leading-relaxed">
                Your success is our success. We're committed to providing exceptional support and ensuring 
                you get the most value from PalmPOS.
              </p>
            </div>
            <div class="p-5 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
              <h3 class="text-base font-semibold text-gray-900 mb-2">🔒 Data security</h3>
              <p class="text-sm text-gray-600 leading-relaxed">
                We take security seriously. Your data is encrypted, backed up regularly, and protected with 
                industry-leading security measures.
              </p>
            </div>
            <div class="p-5 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
              <h3 class="text-base font-semibold text-gray-900 mb-2">🚀 Innovation</h3>
              <p class="text-sm text-gray-600 leading-relaxed">
                We continuously improve PalmPOS with new features and capabilities based on customer feedback 
                and industry trends.
              </p>
            </div>
            <div class="p-5 rounded-lg border border-gray-200 hover:border-gray-300 hover:shadow-sm transition-all duration-200">
              <h3 class="text-base font-semibold text-gray-900 mb-2">🌴 Local focus</h3>
              <p class="text-gray-600">
                As a Mauritian company, we understand local business needs and provide support in a way that 
                works for you.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-r from-palm-600 to-primary-600 text-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          Join Our Growing Community
        </h2>
        <p class="text-xl mb-8 text-palm-50">
          See why businesses across Mauritius choose PalmPOS
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link to="/demo"
             class="px-8 py-4 bg-white text-palm-600 font-bold rounded-lg shadow-lg hover:shadow-xl transition-all duration-300">
            Try Free Demo
          </router-link>
          <router-link to="/contact" 
                       class="px-8 py-4 bg-transparent border-2 border-white text-white font-bold rounded-lg hover:bg-white hover:text-palm-600 transition-all duration-300">
            Contact Us
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const values = [
  {
    icon: '💡',
    title: 'Innovation',
    description: 'We constantly innovate to provide cutting-edge solutions that help your business stay ahead.'
  },
  {
    icon: '🤝',
    title: 'Partnership',
    description: 'We view our customers as partners and work together to achieve mutual success.'
  },
  {
    icon: '✨',
    title: 'Excellence',
    description: 'We strive for excellence in everything we do, from product development to customer support.'
  },
]
</script>
