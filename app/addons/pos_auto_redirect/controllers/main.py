import werkzeug
from odoo import http
from odoo.addons.web.controllers.home import Home
from odoo.http import request


class PosRedirect(Home):

    @http.route('/', type='http', auth='none', website=True)
    def index(self, **kw):
        """Override root URL to redirect directly to web client, bypassing /odoo"""
        if request.session.uid:
            # User is logged in, redirect to dashboard
            return werkzeug.utils.redirect('/app/dashboard', 303)
        else:
            # User not logged in, redirect to login page
            return werkzeug.utils.redirect('/web/login', 303)

    @http.route()
    def web_login(self, redirect=None, **kw):
        response = super().web_login(redirect=redirect, **kw)
        
        if request.session.uid and not redirect:
            return werkzeug.utils.redirect('/app/point-of-sale', 303)
        
        return response

    @http.route(['/odoo/action-point_of_sale.action_client_pos_menu', 
                 '/app/action-point_of_sale.action_client_pos_menu'], 
                type='http', auth='user', website=True)
    def pos_backend_redirect(self, **kw):
        """Redirect POS Backend button directly to dashboard"""
        return werkzeug.utils.redirect('/app/dashboards?dashboard_id=1', 303)
