# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

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



class Cust_data(models.Model):
    _name = 'cust.datas'
    
    name = fields.Char(string='Name')
    login_user = fields.Char(string='Login_user', default=lambda self: self.env.user.login )
    
    @api.constrains('name')
    def _check_unique_name(self):
        names = self.search([('id', '!=', self.id), ('name', '=ilike', self.name)])
        print(names,"product_______")
        if names:
            raise ValidationError(('name already exists!'))    


    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamic_domain', False):
            domain = self._get_dynamic_domains()
            args = domain
            print(args,'=======')
            # print(self.login_user,'-=-=-=-=')
        return super(Cust_data, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def _get_dynamic_domains(self):
        domain = [('login_user', '=', self.env.user.login)]
        return domain   
    
    
    
class Customesr_Data(models.Model):
    _name = 'customer.datas'     
    
    cust = fields.Many2one('cust.datas', string='Cust')    
    name = fields.Char(string='Name')    
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

    cust =  fields.Many2one('cust.datas', string='cust')    
    customers = fields.Many2one('customer.datas', string='customers')    
    product_id = fields.Many2one('products.datas' , string='products') 
    price = fields.Integer(string='Price',required = True) 
    quantity = fields.Integer(string='quantity',required = True) 
    payment_done = fields.Boolean(string='Pyament Done')
    totle = fields.Float(string='Totle', compute = 'calc_ctcs')
    login_user = fields.Char(string='Login_user', default=lambda self: self.env.user.login)
         
    # #  #   for filter data user wise  
            
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self._context.get('dynamict_domaina', False):
            domain = self._get_dynamic_domains()
            args = domain
            print(args,'=======')
            # print(self.login_user,'-=-=-=-=')
        return super(ProductBorrow, self).search(args, offset=offset, limit=limit, order=order, count=count)
            
    @api.model
    def _get_dynamic_domains(self):
        domain = [('login_user', '=', self.env.user.login)]
        return domain   


    def wiz_open(self):
        #  #  both method for call wizard file
        return self.env['ir.actions.act_window']._for_xml_id('custom_borrow_products.demo_update_data_form')
        
        
    @api.depends('quantity', 'price')
    def calc_ctcs(self):
        for ii in self:
            pri = ii.price 
            qty = ii.quantity
            x = qty * pri
            ii.totle = x



    
    
    
    