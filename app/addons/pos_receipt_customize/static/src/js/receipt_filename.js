/** @odoo-module **/

import { onMounted, onWillUnmount } from "@odoo/owl";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { patch } from "@web/core/utils/patch";

// Store original title and current receipt ID
let currentReceiptId = null;

// Function to extract full ticket number from receipt
const extractTicketNumber = () => {
    const receiptElement = document.querySelector('.pos-receipt');
    if (receiptElement) {
        const allDivs = receiptElement.querySelectorAll('div');
        for (const div of allDivs) {
            const text = div.textContent?.trim();
            // Look for Ticket pattern or order numbers
            if (text && text.includes('Ticket') && !text.includes('Powered')) {
                // Extract just the ticket number pattern (e.g., "264-1-0000083")
                const ticketMatch = text.match(/(\d+)-(\d+)-(\d+)/);
                if (ticketMatch) {
                    const ticketNumber = ticketMatch[0].replace(/\s+/g, ''); // Remove any spaces
                    
                    // Format: YYYYMMDD-HHmmss-ticketnumber
                    const now = new Date();
                    const datepart = `${now.getFullYear()}${String(now.getMonth()+1).padStart(2,'0')}${String(now.getDate()).padStart(2,'0')}`;
                    const timepart = `${String(now.getHours()).padStart(2,'0')}${String(now.getMinutes()).padStart(2,'0')}${String(now.getSeconds()).padStart(2,'0')}`;
                    return `${datepart}-${timepart}-${ticketNumber}`;
                }
            }
        }
    }
    return null;
};

// Patch the ReceiptScreen to set custom title when mounted
patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        
        // Set title immediately in setup, before mounting
        const order = this.currentOrder;
        if (order) {
            currentReceiptId = order.name || order.pos_reference || order.tracking_number || order.uid || `Receipt-${Date.now()}`;
            console.log('ReceiptScreen setup - Initial title:', currentReceiptId);
            
            // Set the custom title using the global variable that palmpos_title respects
            window.palmposCustomTitle = currentReceiptId;
        }
        
        onMounted(() => {
            // After mount, try to extract full ticket number from rendered receipt
            setTimeout(() => {
                const fullTicketNumber = extractTicketNumber();
                if (fullTicketNumber) {
                    currentReceiptId = fullTicketNumber;
                    window.palmposCustomTitle = fullTicketNumber;
                    console.log('ReceiptScreen mounted - Updated to full ticket number:', fullTicketNumber);
                } else if (currentReceiptId) {
                    console.log('ReceiptScreen mounted - Keeping title:', currentReceiptId);
                }
            }, 100); // Small delay to ensure receipt is rendered
        });
        
        onWillUnmount(() => {
            console.log('ReceiptScreen unmounting - clearing custom title');
            // Clear custom title when leaving receipt screen
            window.palmposCustomTitle = null;
            currentReceiptId = null;
        });
    }
});

// Add beforeprint event listener
window.addEventListener('beforeprint', () => {
    console.log('Before print event triggered');
    console.log('Current custom title:', window.palmposCustomTitle);
    
    // Try to get the full ticket number
    let orderName = currentReceiptId || extractTicketNumber();
    
    // Fallback to timestamp if nothing found
    if (!orderName) {
        const now = new Date();
        orderName = `Receipt-${now.getFullYear()}${String(now.getMonth()+1).padStart(2,'0')}${String(now.getDate()).padStart(2,'0')}-${String(now.getHours()).padStart(2,'0')}${String(now.getMinutes()).padStart(2,'0')}${String(now.getSeconds()).padStart(2,'0')}`;
    }
    
    console.log('Setting custom title for print:', orderName);
    window.palmposCustomTitle = orderName;
});

window.addEventListener('afterprint', () => {
    console.log('After print - restoring receipt title');
    // Restore to the receipt ID (not "PalmPOS") if still on receipt screen
    if (currentReceiptId) {
        window.palmposCustomTitle = currentReceiptId;
    }
});
