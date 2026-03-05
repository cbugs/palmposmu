/** @odoo-module **/

// Replace "Odoo Point of Sale" with "PalmPOS" in dialogs
const replaceBranding = () => {
    // Find all modal bodies and replace text
    const modalBodies = document.querySelectorAll('.modal-body p, .modal-body');
    modalBodies.forEach(element => {
        if (element.textContent.includes('Odoo Point of Sale')) {
            element.textContent = element.textContent.replace(/Odoo Point of Sale/g, 'PalmPOS');
            console.log('Replaced Odoo Point of Sale with PalmPOS');
        }
    });
};

// Run immediately
replaceBranding();

// Run on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    replaceBranding();
    
    // Create a MutationObserver to watch for dialog changes
    const observer = new MutationObserver((mutations) => {
        let shouldReplace = false;
        
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) { // Element node
                    // Check if this is a modal or contains modal content
                    if (node.classList?.contains('modal') || 
                        node.classList?.contains('modal-content') || 
                        node.classList?.contains('modal-body') ||
                        node.querySelector?.('.modal-body')) {
                        shouldReplace = true;
                    }
                }
            });
        });
        
        if (shouldReplace) {
            // Small delay to ensure content is rendered
            setTimeout(replaceBranding, 50);
        }
    });
    
    // Observe the entire document for changes
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
});

// Also run periodically for the first few seconds after page load
let checkCount = 0;
const intervalId = setInterval(() => {
    replaceBranding();
    checkCount++;
    if (checkCount > 20) { // Stop after 10 seconds (20 * 500ms)
        clearInterval(intervalId);
    }
}, 500);
