from odoo import models ,  fields, api


class RetailProduct(models.Model):
    _name = "retail.product"
    _rec_name = "code"

    my_seq = fields.Char(string='Barcode', readonly=True)
    code = fields.Char(string="Code")
    type = fields.Char(string="Type")

    unit_cost = fields.Float(string="unit cost")
    unit_price = fields.Float(string="unit_price")
    ready_quantity = fields.Integer(string="ready quantity")
    desc_id = fields.One2many("product.description", "product_id" )

    @api.model
    def create(self, vals):
        vals['my_seq'] = self.env['ir.sequence'].next_by_code('code')
        return super(RetailProduct, self).create(vals)


class ProductDescription(models.Model):

    _name = "product.description"
    _rec_name = "size"

    product_id = fields.Many2one("retail.product")
    purchase_id = fields.Many2one("retail.purchase")
    size = fields.Char(string="Size")
    color = fields.Char(string="Color")
    quantity = fields.Integer(string="quantity")
