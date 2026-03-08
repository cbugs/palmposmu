# -*- coding: utf-8 -*-
from odoo import models
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    def action_view_receipt(self):
        """Open the POS receipt screen for this order"""
        self.ensure_one()
        
        # Check if order has a session and config
        if not self.session_id or not self.session_id.config_id:
            raise UserError("Cannot display receipt: Order has no valid POS session.")
        
        # Use the standard uuid field that POS uses for receipts
        if not self.uuid:
            raise UserError("Cannot display receipt: Order has no UUID.")
        
        # Get the config ID
        config_id = self.session_id.config_id.id
        
        # Build the receipt URL using the order's UUID
        receipt_url = f'/pos/ui/{config_id}/receipt/{self.uuid}'
        
        # Return action to open URL
        return {
            'type': 'ir.actions.act_url',
            'url': receipt_url,
            'target': 'new',  # Opens in new tab/window
        }
