from odoo import models, fields


class HmsDoctors(models.Model):
    _name = 'hms.doctors'

    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(required=True)
    image = fields.Image()
    patient_ids = fields.Many2many('hms.patient')


