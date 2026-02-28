// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_URL || window.location.origin;

export const API_ENDPOINTS = {
  CONTACT_SUBMIT: `${API_BASE_URL}/api/contact/submit`,
  PRICING_INQUIRY: `${API_BASE_URL}/api/contact/pricing-inquiry`,
};

export default {
  API_BASE_URL,
  API_ENDPOINTS,
};
