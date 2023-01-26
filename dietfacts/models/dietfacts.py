from odoo import models, fields

# Extend product.template model with calories
class Dietfacts_Product_Template(models.Model):
    _name='product.template'
    _inherit='product.template'
    calories = fields.Integer("Calories")