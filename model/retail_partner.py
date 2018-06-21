from odoo import models ,  fields, api

class RetailPartner(models.Model):
    _name = "retail.partner"

    name = fields.Char(string="Name")
    phone = fields.Char()
