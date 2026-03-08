/** @odoo-module **/
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { AlertDialog, ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";
import { rpc } from "@web/core/network/rpc";
import { patch } from "@web/core/utils/patch";


/*
 * Patching the PosStore class to add custom functionality.
 */
patch(PosStore.prototype, {
    async pay() {
        const currentOrder = this.selectedOrder;
        if (!currentOrder) {
            return;
        }

        let order_name = currentOrder.pos_reference;
        let self = this;
        
        const result = await rpc("/web/dataset/call_kw/pos.order/check_order",{
            model: 'pos.order', method: 'check_order',
            args: [order_name],
            kwargs: {},
        });
        
        if (result.category) {
            let title = "No category found for your current order in the kitchen.(" + result.category + ')';
            await this.env.services.dialog.add(AlertDialog, {
                title: _t(title),
                body: _t("No food items found for the specified category for this kitchen. Kindly remove the selected food and update the order by clicking the 'Order' button. Following that, proceed with the payment."),
            });
            return false;
        } else if (result == true) {
            await this.env.services.dialog.add(AlertDialog, {
                title: _t("Food is not ready"),
                body: _t("Please Complete all the food first."),
            });
            return false;
        }

        if (!currentOrder.canPay()) {
            return;
        }

        if (
            currentOrder.lines.some(
                (line) => line.get_product().tracking !== "none" && !line.has_valid_product_lot()
            ) &&
            (this.pickingType.use_create_lots || this.pickingType.use_existing_lots) && (result == false)
        ) {
            const confirmed = await this.env.services.dialog.add(ConfirmationDialog, {
                title: _t("Some Serial/Lot Numbers are missing"),
                body: _t(
                    "You are trying to sell products with serial/lot numbers, but some of them are not set.\nWould you like to proceed anyway?"
                ),
            });
            if (confirmed) {
                this.mobile_pane = "right";
                this.env.services.pos.showScreen("PaymentScreen", {
                    orderUuid: this.selectedOrderUuid,
                });
            }
        } else {
            this.mobile_pane = "right";
            this.env.services.pos.showScreen("PaymentScreen", {
                orderUuid: this.selectedOrderUuid,
            });
        }
    }
});