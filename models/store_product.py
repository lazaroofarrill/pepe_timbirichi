from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


def is_allowed_transition(old_state, new_state):
    """
    :param old_state: the current state of the product
    :param new_state: the new state of the product
    :return: True if transistion is allowed, otherwise False
    """
    allowed_transitions = [
        ('incoming', 'in_stock'),
        ('in_stock', 'out_of_stock'),
        ('out_of_stock', 'in_stock'),
        ('in_stock', 'discontinued'),
        ('out_of_stock', 'discontinued')
    ]

    return (old_state, new_state) in allowed_transitions


class StoreProduct(models.Model):
    _name = 'store.product'
    _description = 'The Product to be sold in the Store'

    name = fields.Char("Product name", required=True)
    date_release = fields.Date("Release date")
    product_image = fields.Binary("Image")
    description = fields.Html("Description")

    currency_id = fields.Many2one("res.currency", string="Currency")
    retail_price = fields.Monetary("Price", currency_field="currency_id", required=True)

    state = fields.Selection([
        ('incoming', 'Unavailable'),
        ('in_stock', 'In stock'),
        ('out_of_stock', 'Out of stock'),
        ('discontinued', 'Discontinued')
    ], default="incoming")

    # department = fields.Many2one("")
    seller_id = fields.Many2one("res.company", string="Seller")
    manufacturer_id = fields.Many2one("res.company", string="Manufacturer")

    # product.state related methods

    def _change_state(self, new_state):
        """
        :param new_state: the new state for the product

        """
        for product in self:
            if is_allowed_transition(product.state, new_state):
                product.state = new_state
            else:
                msg = _(f'Impossible to change state from {product.state} to {new_state}')
                raise UserError(msg)

    def make_in_stock(self):
        self._change_state('in_stock')

    def make_out_of_stock(self):
        self._change_state('out_of_stock')

    def make_discontinued(self):
        self._change_state('discontinued')

