from odoo import models, fields


class HospitalPatient (models.Model):
    _name= "hospital.patient"
    _inherit= ['mail.thread','mail.activity.mixin']
    _description= "Hospital Patient"

    age= fields.Integer("Age", tracking=True)
    gender= fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True)
    name= fields.Char("Name", tracking=True)
    phone= fields.Char("Phone Number")
    bloodType= fields.Selection([
                                 ('o_pos',"O +ve"), ('o_neg','O -ve'),
                                 ('a_pos','A +ve'), ('a_neg','A -ve'),
                                 ('ab_pos','AB +ve'), ('ab_neg','AB -ve'),
                                 ])
    active= fields.Boolean(string="Active",default=True)
