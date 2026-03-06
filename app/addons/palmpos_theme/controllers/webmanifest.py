# -*- coding: utf-8 -*-
from urllib.parse import unquote

from odoo import http
from odoo.addons.web.controllers.webmanifest import WebManifest
from odoo.http import request


class PalmPOSWebManifest(WebManifest):
    
    def _get_scoped_app_icons(self, app_id):
        """Override to use PalmPOS logo for Point of Sale app"""
        if app_id == 'point_of_sale':
            return [
                {
                    'src': '/palmpos_theme/static/img/logo.webp',
                    'sizes': '512x512',
                    'type': 'image/webp',
                    'purpose': 'any'
                },
                {
                    'src': '/palmpos_theme/static/img/logo.webp',
                    'sizes': '192x192',
                    'type': 'image/webp',
                    'purpose': 'maskable'
                }
            ]
        return super()._get_scoped_app_icons(app_id)
    
    @http.route('/web/manifest.webmanifest', type='http', auth='public', methods=['GET'], sitemap=False)
    def webmanifest(self):
        """Override general webmanifest to use PalmPOS branding"""
        webmanifest = {
            'name': 'PalmPOS',
            'short_name': 'PalmPOS',
            'description': 'Point of Sale and Inventory Management System',
            'scope': '/',
            'start_url': '/app/point-of-sale',
            'display': 'standalone',
            'background_color': '#ffffff',
            'theme_color': '#10b981',
            'icons': [
                {
                    'src': '/palmpos_theme/static/img/logo.webp',
                    'sizes': '512x512',
                    'type': 'image/webp',
                    'purpose': 'any'
                },
                {
                    'src': '/palmpos_theme/static/img/logo.webp',
                    'sizes': '192x192',
                    'type': 'image/webp',
                    'purpose': 'maskable'
                }
            ]
        }
        return request.make_json_response(webmanifest, {
            'Content-Type': 'application/manifest+json'
        })
    
    @http.route('/web/manifest.scoped_app_manifest', type='http', auth='public', methods=['GET'])
    def scoped_app_manifest(self, app_id, path, app_name=''):
        """Override to use PalmPOS green theme color"""
        path = unquote(path)
        
        # Use PalmPOS as the app name for point_of_sale
        if not app_name and app_id == 'point_of_sale':
            app_name = 'PalmPOS'
        elif not app_name:
            app_name = self._get_scoped_app_name(app_id)
        else:
            app_name = unquote(app_name)
        
        webmanifest = {
            'icons': self._get_scoped_app_icons(app_id),
            'name': app_name,
            'short_name': 'PalmPOS' if app_id == 'point_of_sale' else app_name,
            'scope': path,
            'start_url': path,
            'display': 'standalone',
            'background_color': '#ffffff',
            'theme_color': '#10b981',
            'prefer_related_applications': False,
            'shortcuts': self._get_scoped_app_shortcuts(app_id)
        }
        return request.make_json_response(webmanifest, {
            'Content-Type': 'application/manifest+json'
        })
