from odoo import fields, models


class StoreDepartment(models.Model):
    _name = 'store.department'

    name = fields.Char("Department", required=True)
    product_ids = fields.One2many("store.product", 'department_id', string="Products")
    image = fields.Binary("Image")
    description = fields.Html("Description")


