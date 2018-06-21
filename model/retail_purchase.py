
from odoo import models,  fields, api


class RetailPurchase(models.Model):
    _name = "retail.purchase"

    vendor = fields.Many2one("retail.partner")
    phone = fields.Char("Phone #")
    # is_purchase = fields.Boolean(default=True)
    product_id = fields.Many2one("retail.product")
    my_seq = fields.Char(string='Purchase Number', readonly=True)
    type = fields.Char(string="Type")
    unit_cost = fields.Float("Unit Cost")
    quantity = fields.Integer("Purchased quantity")
    desc_id = fields.One2many("product.description", "purchase_id")
    date = fields.Datetime("DATE AND TIME", default=lambda self: fields.datetime.now())

    @api.onchange("vendor")
    def _onchange_to_phone(self):
        self.phone=self.vendor.phone

    @api.onchange("product_id")
    def _product_id_parameter(self):
        products = self.env['retail.product'].search([('code', '=', self.product_id.code)])
        for product in products:
            self.type = product.type
            self.unit_cost = product.unit_cost
            self.quantity = product.ready_quantity

    @api.onchange("quantity")
    def _product_id_change(self):
        products = self.env['retail.product'].search([('code', '=', self.product_id.code)])
        for product in products:
            # product.unit_cost = self.unit_cost
            product.write({"ready_quantity ": self.quantity})

    @api.model
    def create(self, vals):
        vals['my_seq'] = self.env['ir.sequence'].next_by_code('code')
        return super(RetailPurchase, self).create(vals)