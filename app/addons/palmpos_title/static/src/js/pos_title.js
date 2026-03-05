/** @odoo-module **/

// Global variable to track if we should use a custom title (e.g., for receipts)
window.palmposCustomTitle = null;

// Function to set title - only update if custom title is not set or title doesn't match
const setPalmPOSTitle = () => {
    // If custom title is set, use it; otherwise use PalmPOS
    const targetTitle = window.palmposCustomTitle || 'PalmPOS';
    
    // Only update if different
    if (document.title !== targetTitle) {
        document.title = targetTitle;
        console.log('Title updated to:', targetTitle);
    }
};

// Set immediately
setPalmPOSTitle();

// Update favicon for POS
const updateFavicon = () => {
    // Remove existing favicons
    const existingIcons = document.querySelectorAll('link[rel*="icon"]');
    existingIcons.forEach(icon => icon.remove());

    // Add new favicon
    const favicon = document.createElement('link');
    favicon.rel = 'icon';
    favicon.type = 'image/x-icon';
    favicon.href = '/palmpos_title/static/img/logo.webp';
    document.head.appendChild(favicon);
};

// Update favicon on load
updateFavicon();

// Watch for changes to palmposCustomTitle
let lastCustomTitle = null;
const checkTitleInterval = setInterval(() => {
    // Only update if custom title changed or if no custom title and current title is wrong
    if (window.palmposCustomTitle !== lastCustomTitle) {
        lastCustomTitle = window.palmposCustomTitle;
        setPalmPOSTitle();
    } else if (!window.palmposCustomTitle && document.title !== 'PalmPOS') {
        // Only force back to PalmPOS if there's no custom title
        setPalmPOSTitle();
    }
}, 200);

// Set on various events
window.addEventListener('load', setPalmPOSTitle);
document.addEventListener('DOMContentLoaded', setPalmPOSTitle);
