from odoo import models, fields


# Extend product.template model with calories
class DietfactsProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    calories = fields.Integer("Calories",default=0)
