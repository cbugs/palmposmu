# -*- coding: utf-8 -*-
from urllib.parse import unquote

from odoo import http
from odoo.addons.web.controllers.webmanifest import WebManifest
from odoo.http import request


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
    
    @http.route('/web/manifest.scoped_app_manifest', type='http', auth='public', methods=['GET'])
    def scoped_app_manifest(self, app_id, path, app_name=''):
        """Override to use PalmPOS green theme color"""
        path = unquote(path)
        app_name = unquote(app_name) if app_name else self._get_scoped_app_name(app_id)
        
        webmanifest = {
            'icons': self._get_scoped_app_icons(app_id),
            'name': app_name,
            'scope': path,
            'start_url': path,
            'display': 'standalone',
            'background_color': '#059669',
            'theme_color': '#059669',
            'prefer_related_applications': False,
            'shortcuts': self._get_scoped_app_shortcuts(app_id)
        }
        return request.make_json_response(webmanifest, {
            'Content-Type': 'application/manifest+json'
        })
