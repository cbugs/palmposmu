/** @odoo-module **/

import { onMounted } from "@odoo/owl";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { patch } from "@web/core/utils/patch";

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        
        onMounted(() => {
            // Add WhatsApp button to the receipt screen
            this.addWhatsAppButton();
        });
    },
    
    addWhatsAppButton() {
        // Find the button container
        const buttonContainer = document.querySelector('.receipt-screen .button-container');
        if (buttonContainer) {
            // Check if button already exists
            if (buttonContainer.querySelector('.btn-send-whatsapp')) {
                return;
            }
            
            // Create the button
            const whatsappBtn = document.createElement('button');
            whatsappBtn.className = 'btn btn-success btn-send-whatsapp';
            whatsappBtn.innerHTML = '<i class="fa fa-whatsapp"></i> Send via WhatsApp';
            whatsappBtn.onclick = () => this.sendWhatsApp();
            
            // Add to container
            buttonContainer.appendChild(whatsappBtn);
        }
    },
    
    sendWhatsApp() {
        const order = this.currentOrder;
        if (!order) return;
        
        // Get receipt details
        const receiptNumber = window.palmposCustomTitle || order.name || 'Receipt';
        const orderTotal = order.get_total_with_tax().toFixed(2);
        const orderDate = new Date().toLocaleString();
        
        // Get business name from POS config
        const businessName = this.pos.config.name || 'PalmPOS';
        
        // Create receipt URL - you can modify this based on your setup
        // For now, we'll create a message with receipt details
        const message = `*${businessName}*\n\n` +
                       `Receipt: ${receiptNumber}\n` +
                       `Date: ${orderDate}\n` +
                       `Total: ${order.currency.symbol}${orderTotal}\n\n` +
                       `Thank you for your business!`;
        
        // Encode message for URL
        const encodedMessage = encodeURIComponent(message);
        
        // Open WhatsApp with pre-filled message
        // Using web.whatsapp.com for desktop, or wa.me for mobile
        const whatsappUrl = `https://wa.me/?text=${encodedMessage}`;
        
        // Open in new window
        window.open(whatsappUrl, '_blank');
    }
});
