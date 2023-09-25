# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http,  _
from odoo.addons.web.controllers.home import Home
from odoo.http import request
import json
from werkzeug.wrappers import Response


class ProductManagementHome(Home):

    @http.route('/api/product', auth='none', type='json',method=['POST'])
    def api_product(self, *args, **kw):

        fields = kw.get('fields')
        domain = kw.get('domain')

        data = request.env['product'].sudo().search_read(domain,fields)
        
        return data