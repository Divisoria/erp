from odoo import models, fields, api, http


class Product(models.Model):
    _name = 'product'
    _description = 'Product'

    name = fields.Char(required=True)
    description = fields.Text(required=True)
    price = fields.Float()
    image = fields.Image(string="Image", store=True)