# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http , SUPERUSER_ID
from odoo.addons.web.controllers.home import Home
from odoo.http import request
import json
from werkzeug.wrappers import Response


class AccountManagementHome(Home):
    
    @http.route('/api/signup', auth='none', type='json', method=['POST'], csrf=False)
    def api_sign_up(self, *args, **kw):
        name = kw['name']
        login = kw['login']
        password = kw['password']

        request.env['res.users'].with_user(SUPERUSER_ID).sudo().signup({
            "name": name,
            "login": login,
            "password": password,
        })
        
        return {"message": "Success"}
