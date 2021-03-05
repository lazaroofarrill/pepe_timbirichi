from odoo import fields, models, api


class StoreSeller(models.Model):
    _name = 'store.seller'
    _inherit = 'res.partner'

    name = fields.Char("Seller")
    product_ids = fields.One2many('store.product', 'seller_id', string='Seller')
