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
        
        onMounted(() => {
            // After mount, set the title
            const order = this.currentOrder;
            if (order) {
                currentReceiptId = order.name || order.pos_reference || order.tracking_number || order.uid || `Receipt-${Date.now()}`;
                console.log('ReceiptScreen mounted - Initial title:', currentReceiptId);
                
                // Set the custom title using the global variable that palmpos_title respects
                window.palmposCustomTitle = currentReceiptId;
                
                // Try to extract full ticket number from rendered receipt
                setTimeout(() => {
                    const fullTicketNumber = extractTicketNumber();
                    if (fullTicketNumber) {
                        currentReceiptId = fullTicketNumber;
                        window.palmposCustomTitle = fullTicketNumber;
                        console.log('ReceiptScreen - Updated to full ticket number:', fullTicketNumber);
                    }
                }, 200); // Small delay to ensure receipt is rendered
            }
            
            // Add WhatsApp button with multiple retries and broader selectors
            setTimeout(() => {
                this.addWhatsAppButton();
            }, 500);
        });
        
        onWillUnmount(() => {
            console.log('ReceiptScreen unmounting - clearing custom title');
            // Clear custom title when leaving receipt screen
            window.palmposCustomTitle = null;
            currentReceiptId = null;
        });
    },
    
    addWhatsAppButton() {
        let attempts = 0;
        const maxAttempts = 15;
        
        const tryAddButton = () => {
            // Try multiple selectors to find where buttons are
            let buttonContainer = document.querySelector('.receipt-screen .button-container');
            
            if (!buttonContainer) {
                // Try alternative selectors
                buttonContainer = document.querySelector('.receipt-screen div[class*="button"]');
            }
            
            if (!buttonContainer) {
                // Find any button and get its parent
                const existingButton = document.querySelector('.receipt-screen button');
                if (existingButton) {
                    buttonContainer = existingButton.parentElement;
                }
            }
            
            if (buttonContainer) {
                // Check if button already exists
                if (buttonContainer.querySelector('.btn-send-whatsapp')) {
                    console.log('WhatsApp button already exists');
                    return;
                }
                
                // Create the WhatsApp button
                const whatsappBtn = document.createElement('button');
                whatsappBtn.className = 'btn btn-success btn-send-whatsapp';
                whatsappBtn.innerHTML = '<i class="fa fa-whatsapp"></i> Send via WhatsApp';
                whatsappBtn.onclick = () => this.sendWhatsApp();
                
                // Add button to container
                buttonContainer.appendChild(whatsappBtn);
                console.log('✅ WhatsApp button successfully added!');
            } else {
                attempts++;
                if (attempts < maxAttempts) {
                    console.log(`Retry ${attempts}/${maxAttempts} - looking for button container...`);
                    setTimeout(tryAddButton, 200);
                } else {
                    console.error('❌ Could not find button container after', maxAttempts, 'attempts');
                    // Log what's available
                    const receiptScreen = document.querySelector('.receipt-screen');
                    if (receiptScreen) {
                        console.log('Receipt screen HTML:', receiptScreen.innerHTML.substring(0, 500));
                    }
                }
            }
        };
        
        tryAddButton();
    },
    
    sendWhatsApp() {
        const order = this.currentOrder;
        if (!order) {
            console.log('No order found for WhatsApp');
            return;
        }
        
        // Get receipt details
        const receiptNumber = window.palmposCustomTitle || order.name || 'Receipt';
        const orderTotal = (order.get_total_with_tax ? order.get_total_with_tax() : order.amount_total || 0).toFixed(2);
        const orderDate = new Date().toLocaleString();
        
        // Get business name and currency from POS config
        const businessName = this.pos.config.name || 'PalmPOS';
        const currency = this.pos.currency || {};
        const currencySymbol = currency.symbol || '$';
        
        // Build order items list
        let itemsText = '';
        if (order.lines && order.lines.length > 0) {
            itemsText = '\n*Order Items:*\n';
            itemsText += '━━━━━━━━━━━━━━━━\n';
            
            // Limit to first 5 items to keep message under 1000 chars
            const maxItems = 5;
            const lines = order.lines.slice(0, maxItems);
            
            lines.forEach(line => {
                let productName = line.product_id?.display_name || line.get_product()?.display_name || 'Product';
                // Truncate long product names to 40 chars
                if (productName.length > 40) {
                    productName = productName.substring(0, 37) + '...';
                }
                const qty = line.quantity || line.qty || 1;
                const price = (line.price_subtotal_incl || line.get_all_prices?.()?.priceWithTax || 0).toFixed(2);
                
                itemsText += `${qty}x ${productName}\n`;
                itemsText += `   ${currencySymbol}${price}\n`;
            });
            
            if (order.lines.length > maxItems) {
                itemsText += `\n... and ${order.lines.length - maxItems} more items\n`;
            }
            itemsText += '━━━━━━━━━━━━━━━━\n';
        }
        
        // Create receipt message with items
        const message = `*${businessName}*\n` +
                       `━━━━━━━━━━━━━━━━\n\n` +
                       `*Receipt #${receiptNumber}*\n` +
                       `${orderDate}` +
                       itemsText +
                       `\n*Total: ${currencySymbol}${orderTotal}*\n\n` +
                       `Thank you for your business!`;
        
        // Encode message for URL
        const encodedMessage = encodeURIComponent(message);
        
        // Open WhatsApp with pre-filled message
        const whatsappUrl = `https://wa.me/?text=${encodedMessage}`;
        
        console.log('Opening WhatsApp with message:', message);
        
        // Open in new window
        window.open(whatsappUrl, '_blank');
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
