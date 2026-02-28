/** @odoo-module **/

// Function to set title
const setPalmPOSTitle = () => {
    if (document.title !== 'PalmPOS') {
        document.title = 'PalmPOS';
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

// Force title update every 100ms for the first 5 seconds
let counter = 0;
const aggressiveInterval = setInterval(() => {
    setPalmPOSTitle();
    counter++;
    if (counter > 50) { // After 5 seconds (50 * 100ms)
        clearInterval(aggressiveInterval);
        // Then check every second
        setInterval(setPalmPOSTitle, 1000);
    }
}, 100);

// Watch for any title changes and force it back to PalmPOS
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        setPalmPOSTitle();
    });
});

// Observe changes to the title element
const titleElement = document.querySelector('title');
if (titleElement) {
    observer.observe(titleElement, { 
        childList: true,
        characterData: true,
        subtree: true 
    });
}

// Set on various events
window.addEventListener('load', setPalmPOSTitle);
document.addEventListener('DOMContentLoaded', setPalmPOSTitle);

// Override title property (might not work in all cases due to Odoo's framework)
try {
    const originalTitleDesc = Object.getOwnPropertyDescriptor(Document.prototype, 'title');
    Object.defineProperty(document, 'title', {
        get: function() {
            return 'PalmPOS';
        },
        set: function(newTitle) {
            // Always return PalmPOS, ignore attempts to change
            if (originalTitleDesc && originalTitleDesc.set) {
                originalTitleDesc.set.call(this, 'PalmPOS');
            }
        },
        configurable: true
    });
} catch(e) {
    console.log('Could not override title property:', e);
}
