/** @odoo-module **/

// Replace "Odoo Point of Sale" with "PalmPOS" in dialogs
document.addEventListener('DOMContentLoaded', () => {
    // Create a MutationObserver to watch for dialog changes
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) { // Element node
                    // Check for connection lost dialog
                    const modalTitle = node.querySelector('.modal-title');
                    const modalBody = node.querySelector('.modal-body p');
                    
                    if (modalTitle && modalTitle.textContent.includes('Connection Lost')) {
                        if (modalBody) {
                            modalBody.textContent = modalBody.textContent.replace(
                                'Odoo Point of Sale', 
                                'PalmPOS'
                            );
                        }
                    }
                    
                    // Also check within the node itself
                    if (node.classList && (node.classList.contains('modal-content') || node.classList.contains('modal-body'))) {
                        const paragraphs = node.querySelectorAll('p');
                        paragraphs.forEach(p => {
                            if (p.textContent.includes('Odoo Point of Sale')) {
                                p.textContent = p.textContent.replace('Odoo Point of Sale', 'PalmPOS');
                            }
                        });
                    }
                }
            });
        });
    });
    
    // Observe the entire document for changes
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
});
