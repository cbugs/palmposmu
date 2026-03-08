/** @odoo-module **/

import { onMounted } from "@odoo/owl";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { patch } from "@web/core/utils/patch";

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        
        onMounted(() => {
            // Add WhatsApp button with retry logic
            setTimeout(() => {
                this.addWhatsAppButton();
            }, 500);
        });
    },
    
    addWhatsAppButton() {
        let attempts = 0;
        const maxAttempts = 15;
        
        const tryAddButton = () => {
            // Find the receipt-options container
            const receiptOptions = document.querySelector('.receipt-options');
            
            if (receiptOptions) {
                // Check if button already exists
                if (receiptOptions.querySelector('.btn-send-whatsapp')) {
                    return;
                }
                
                // Create a wrapper div for the button
                const buttonWrapper = document.createElement('div');
                buttonWrapper.className = 'd-flex gap-1';
                
                // Create the WhatsApp button
                const whatsappBtn = document.createElement('button');
                whatsappBtn.className = 'btn btn-success btn-send-whatsapp w-100 py-3';
                whatsappBtn.innerHTML = '<i class="fa fa-whatsapp"></i> Send via WhatsApp';
                whatsappBtn.onclick = () => this.sendWhatsApp();
                
                // Add button to wrapper
                buttonWrapper.appendChild(whatsappBtn);
                
                // Insert after the email section (which is the second child)
                const emailSection = receiptOptions.querySelector('.d-flex.flex-column.gap-2');
                if (emailSection) {
                    emailSection.insertAdjacentElement('afterend', buttonWrapper);
                } else {
                    // Fallback: add at the end
                    receiptOptions.appendChild(buttonWrapper);
                }
            } else {
                attempts++;
                if (attempts < maxAttempts) {
                    setTimeout(tryAddButton, 200);
                }
            }
        };
        
        tryAddButton();
    },
    
    sendWhatsApp() {
        const order = this.currentOrder;
        if (!order) {
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
        
        // Get footer message from config or use default
        const footerMessage = this.pos.config.receipt_footer_message || 'Thank you for your business!';
        
        // Create receipt message with items
        const message = `*${businessName}*\n` +
                       `━━━━━━━━━━━━━━━━\n\n` +
                       `*Receipt #${receiptNumber}*\n` +
                       `${orderDate}` +
                       itemsText +
                       `\n*Total: ${currencySymbol}${orderTotal}*\n\n` +
                       `${footerMessage}`;
        
        // Encode message for URL
        const encodedMessage = encodeURIComponent(message);
        
        // Open WhatsApp with pre-filled message
        const whatsappUrl = `https://wa.me/?text=${encodedMessage}`;
        
        // Open in new window
        window.open(whatsappUrl, '_blank');
    }
});
