import werkzeug
from odoo import http
from odoo.addons.web.controllers.home import Home
from odoo.http import request


class PosRedirect(Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        response = super().web_login(redirect=redirect, **kw)
        
        if request.session.uid and not redirect:
            return werkzeug.utils.redirect('/app/point-of-sale', 303)
        
        return response
