# -*- coding: utf-8 -*-

from odoo import models, fields, api

# abc
class custom_borrow_products(models.Model):
    _name = 'custom_borrow_products.custom_borrow_products'
    _description = 'custom_borrow_products.custom_borrow_products'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class Products(models.Model):
    _name = 'products.datas'
    _description = 'products detailes'
    _order  =  'name'

    name  = fields.Char(string='Name')


class Customesr_Data(models.Model):
    _name = 'customer.datas'     
    
    name = fields.Char(string='Name',required = True)    
    productsborrows = fields.One2many('product.borrows', 'customers' , string='Productsborrows')
    login_user = fields.Char(string='Login_user', default=lambda self: self.env.user.login )

    
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamict_domain', False):
            domain = self._get_dynamic_domains()
            args = domain
            print(args,'=======')
            # print(self.login_user,'-=-=-=-=')
        return super(Customesr_Data, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def _get_dynamic_domains(self):
        domain = [('login_user', '=', self.env.user.login)]
        return domain   



class ProductBorrow(models.Model):  
    _name = 'product.borrows'  

    customers = fields.Many2one('customer.datas', string='customers')    
    product_id = fields.Many2one('products.datas' , string='products') 
    price = fields.Integer(string='Price',required = True) 
    quantity = fields.Integer(string='quantity',required = True) 
    payment_done = fields.Boolean(string='Pyament Done')
    def check_data(self):
        
        
        # query = """
        #     SELECT customers, SUM(price) as total_sales
        #     FROM sale_order
        #     WHERE state = 'sale'
        #     GROUP BY user_id
        # """   
        
        x = self.env['product.borrows'].search([('customers', '=', self.customers.name)])
        print(x,'-=-=-=-=-==-=--=-')
        xx = []
        for i in x:
            p = i.price
            if i.payment_done == False:
                xx.append(p)       
        print(sum(xx),'-=-=-==-')    
        print("this is it for new data... ")

    
    
    
    
    