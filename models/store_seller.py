from odoo import fields, models


class StoreSeller(models.Model):
    _name = 'store.seller'

    name = fields.Char("Seller")
    website = fields.Char("Website link")
    image = fields.Binary('Image')
    product_ids = fields.One2many('store.product', 'seller_id', string='Seller')
