from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/pepe_timbirichi/products')
    def products(self):
        products = request.env['store.product'].sudo().search([])
        html_result = '<html><body><ul>'

        for product in products:
            html_result += f"<li>{product.name}</li>"

        html_result += '</ul></body></html>'
        return html_result

    @http.route('/pepe_timbirichi/products/json', type='json', auth='none')
    def products_json(self):
        records = request.env['store.product'].sudo().search([])
        return records.read(['name'])


