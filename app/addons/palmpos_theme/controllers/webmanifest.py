# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.webmanifest import WebManifest


class PalmPOSWebManifest(WebManifest):
    
    def _get_scoped_app_icons(self, app_id):
        """Override to use PalmPOS logo for Point of Sale app"""
        if app_id == 'point_of_sale':
            return [{
                'src': '/palmpos_theme/static/img/logo.webp',
                'sizes': 'any',
                'type': 'image/webp',
                'purpose': 'any maskable'
            }]
        return super()._get_scoped_app_icons(app_id)
