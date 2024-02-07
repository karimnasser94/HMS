from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HmsPatient(models.Model):
    _name = 'hms.patient'

    name = fields.Char(string='First Name')
    lastname = fields.Char(string='Last Name')
    email = fields.Char()
    birthdate = fields.Date(string=' Birth date')
    history = fields.Html(string=' History')
    cr_ratio = fields.Float(string=' CR Ratio')
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB'),

    ])
    pcr = fields.Boolean(string='PCR')
    image = fields.Image(string='Image')
    address = fields.Text(string='Address')
    age = fields.Integer(string='Age')


    



