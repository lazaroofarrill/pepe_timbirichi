from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StoreProductDepartment(models.Model):
    _name = 'store.product.department'
    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'
    parent_path = fields.Char(index=True)

    name = fields.Char("Department", required=True)
    parent_id = fields.Many2one('store.product.department', string='Parent Department',
                                ondelete='restrict', index=True)
    product_ids = fields.One2many('store.product.department', 'parent_id', string='Products')
    # product_ids = fields.One2many("store.product", 'department_id', string="Products")
    image = fields.Binary("Image")
    description = fields.Html("Description")

    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories')


