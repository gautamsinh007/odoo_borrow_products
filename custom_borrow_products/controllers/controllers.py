# -*- coding: utf-8 -*-
from odoo import http


class CustomBorrowProducts(http.Controller):
    @http.route('/custom_borrow_products/custom_borrow_products', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/custom_borrow_products/custom_borrow_products/objects', auth='public')
    def list(self, **kw):
        return http.request.render('custom_borrow_products.listing', {
            'root': '/custom_borrow_products/custom_borrow_products',
            'objects': http.request.env['custom_borrow_products.custom_borrow_products'].search([]),
        })

    @http.route('/custom_borrow_products/custom_borrow_products/objects/<model("custom_borrow_products.custom_borrow_products"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('custom_borrow_products.object', {
            'object': obj
        })
