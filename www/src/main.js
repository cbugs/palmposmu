import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

// Import views
import About from './views/About.vue'
import Contact from './views/Contact.vue'
import Demo from './views/Demo.vue'
import Features from './views/Features.vue'
import Home from './views/Home.vue'
import Pricing from './views/Pricing.vue'
import Privacy from './views/Privacy.vue'
import Terms from './views/Terms.vue'

const routes = [
  { 
    path: '/', 
    name: 'Home', 
    component: Home,
    meta: {
      title: 'PalmPOS - Point of Sale System for Mauritius | Retail & Restaurant POS',
      description: 'Complete POS solution designed for Mauritian businesses. Manage sales, inventory, customers & payments. Perfect for retail stores, restaurants, cafes.'
    }
  },
  { 
    path: '/features', 
    name: 'Features', 
    component: Features,
    meta: {
      title: 'Features - PalmPOS Mauritius | POS System Capabilities',
      description: 'Discover PalmPOS features: inventory management, sales tracking, customer loyalty, multi-location support, reporting & analytics for Mauritius businesses.'
    }
  },
  { 
    path: '/pricing', 
    name: 'Pricing', 
    component: Pricing,
    meta: {
      title: 'Pricing - PalmPOS Mauritius | Affordable POS Plans',
      description: 'Transparent pricing for PalmPOS in Mauritius. Plans starting from Rs 2,500/month. Compare features for retail stores, restaurants and enterprises.'
    }
  },
  { 
    path: '/demo', 
    name: 'Demo', 
    component: Demo,
    meta: {
      title: 'Free Demo - PalmPOS Mauritius | Try Our POS System',
      description: 'Request a free demo of PalmPOS. See how our point of sale system can streamline your Mauritius business operations. No credit card required.'
    }
  },
  { 
    path: '/about', 
    name: 'About', 
    component: About,
    meta: {
      title: 'About Us - PalmPOS Mauritius | Local POS Provider',
      description: 'Learn about Palmtree Mauritius, the team behind PalmPOS. Dedicated to empowering local businesses with modern technology solutions.'
    }
  },
  { 
    path: '/privacy', 
    name: 'Privacy', 
    component: Privacy,
    meta: {
      title: 'Privacy Policy - PalmPOS Mauritius',
      description: 'PalmPOS privacy policy. Learn how we protect your business data and customer information in compliance with Mauritius regulations.'
    }
  },
  { 
    path: '/terms', 
    name: 'Terms', 
    component: Terms,
    meta: {
      title: 'Terms of Service - PalmPOS Mauritius',
      description: 'PalmPOS terms of service. Review our service agreement for businesses in Mauritius.'
    }
  },
  { 
    path: '/contact', 
    name: 'Contact', 
    component: Contact,
    meta: {
      title: 'Contact Us - PalmPOS Mauritius | Get Support',
      description: 'Contact PalmPOS Mauritius for sales inquiries, technical support, or demo requests. Email, phone, and office locations in Port Louis.'
    }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

// Update meta tags on route change for better SEO
router.beforeEach((to, from, next) => {
  // Update page title
  document.title = to.meta.title || 'PalmPOS - Point of Sale System for Mauritius'
  
  // Update meta description
  const descriptionMeta = document.querySelector('meta[name="description"]')
  if (descriptionMeta && to.meta.description) {
    descriptionMeta.setAttribute('content', to.meta.description)
  }
  
  // Update Open Graph meta tags
  const ogTitle = document.querySelector('meta[property="og:title"]')
  if (ogTitle && to.meta.title) {
    ogTitle.setAttribute('content', to.meta.title)
  }
  
  const ogDescription = document.querySelector('meta[property="og:description"]')
  if (ogDescription && to.meta.description) {
    ogDescription.setAttribute('content', to.meta.description)
  }
  
  const twitterTitle = document.querySelector('meta[property="twitter:title"]')
  if (twitterTitle && to.meta.title) {
    twitterTitle.setAttribute('content', to.meta.title)
  }
  
  const twitterDescription = document.querySelector('meta[property="twitter:description"]')
  if (twitterDescription && to.meta.description) {
    twitterDescription.setAttribute('content', to.meta.description)
  }
  
  next()
})

const app = createApp(App)
app.use(router)
app.mount('#app')
