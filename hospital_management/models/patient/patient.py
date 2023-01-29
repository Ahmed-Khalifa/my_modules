from odoo import models, fields


class HospitalPatient (models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    age = fields.Integer("Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    name = fields.Char("Name")
    phone= fields.Text("Phone Number")
