/** @odoo-module **/

// Set the document title to PalmPOS for backend
document.title = "PalmPOS";

// Simple interval to maintain title
setInterval(() => {
    if (document.title !== 'PalmPOS') {
        document.title = 'PalmPOS';
    }
}, 1000);
