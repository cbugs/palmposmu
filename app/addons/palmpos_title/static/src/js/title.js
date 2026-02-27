/** @odoo-module **/


// Set the document title to PalmPOS
const originalTitle = document.title;

// Override the title immediately
document.title = "PalmPOS";

// Watch for any title changes and force it back to PalmPOS
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.type === 'childList' && document.title !== 'PalmPOS') {
            document.title = 'PalmPOS';
        }
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

// Also override using Object.defineProperty for more robust control
Object.defineProperty(document, 'title', {
    get: function() {
        return 'PalmPOS';
    },
    set: function(newTitle) {
        // Ignore any attempts to change the title
        return 'PalmPOS';
    },
    configurable: true
});
