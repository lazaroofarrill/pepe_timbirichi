from odoo import fields, models, api


class StoreProduct(models.Model):
    _name = 'store.product'
    _description = 'The Product to be sold in the Store'

    name = fields.Char("Product name", required=True)
    date_release = fields.Date("Release date")
    product_image = fields.Binary("Image")
    description = fields.Html("Description")
    currency_id = fields.Many2one("res.currency", string="Currency")
    retail_price = fields.Monetary("Price", currency_field="currency_id", required=True)
    # department = fields.Many2one("")
    seller_ids = fields.Many2many("res.company", string="Seller")
    # manufacturer_id = fields.Many2one("res.company", string="Manufacturer")

