from odoo import api, fields, models


class RetailProductLine(models.Model):
    _name = "retail.product.line"

    product_id = fields.Many2one("retail.product",string="item")
    type = fields.Char(string="Type")
    sale_order_id = fields.Many2one("retail.sale.order")
    unit_cost = fields.Float(string="unit cost")
    unit_price = fields.Float(string="unit_price")
    sale_quantity = fields.Integer(string="sale quantity")
    purchase_quantity = fields.Integer(string="purchase quantity")

    discount_amount = fields.Float("Discount ..")
    discount_percent = fields.Float("Discount %")

    total_price_before = fields.Float("price", readonly=True)
    total_price_after = fields.Float("final price", readonly=True)

    size = fields.Char(string="Size")
    color = fields.Char(string="Color")
    quantity = fields.Integer(string="quantity")

    @api.onchange("product_id")
    def _onchange_product_id(self):
        products_env = self.env['retail.product'].search([('code', '=', self.product_id.code)])
        for product in products_env:
            self.unit_cost = product.unit_cost
            self.unit_price = product.unit_price
            self.type = product.type

    @api.onchange("sale_quantity")
    def _onchange_quantity_id(self):
        products_env = self.env['retail.product'].search([('code', '=', self.product_id.code)])
        for product in products_env:
            self.total_price_before = self.sale_quantity*product.unit_price
            self.total_price_after = self.total_price_before

    @api.onchange("discount_amount")
    def _onchange_discount_amount(self):
        if self.total_price_before > 0:
            self.discount_percent = 100*self.discount_amount/self.total_price_before
            self.total_price_after = self.total_price_before - self.discount_amount

    @api.onchange("discount_percent")
    def _onchange_discount_percent(self):
        if self.total_price_before > 0:
            if self.discount_amount == 0:
                self.discount_amount = self.discount_percent*self.total_price_before/100
                self.total_price_after = self.total_price_before - self.discount_amount
