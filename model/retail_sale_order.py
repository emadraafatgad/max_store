from odoo import fields, api, models


class RetailSaleOrder(models.Model):
    _name = "retail.sale.order"
    _rec_name = "my_seq"
    my_seq = fields.Char(string='sale number', readonly=True)
    sale_qnt = fields.Integer("Number")
    customer = fields.Many2one("retail.partner")
    phone = fields.Char("Phone")
    date = fields.Datetime("DATE AND TIME", default=lambda self: fields.datetime.now())
    total_price = fields.Float("Total", computed="_compute_total_price", store=True)
    product_line_id = fields.One2many("retail.product.line", "sale_order_id")

    @api.depends('product_line_id.total_price_after')
    def _compute_total_price(self):
            for line in self.product_line_id:
                self.total_price += line.total_price_after

    @api.onchange("customer")
    def _change_phone(self):
        self.phone = self.customer.phone

    @api.model
    def create(self, vals):
        vals['my_seq'] = self.env['ir.sequence'].next_by_code('code')
        return super(RetailSaleOrder, self).create(vals)

