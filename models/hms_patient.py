from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


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
    age = fields.Integer(string='Age', compute='calc_age')
    department_id = fields.Many2one('hms.department')
    capacity = fields.Integer(related='department_id.capacity')
    doctors_ids = fields.Many2many('hms.doctors')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),

    ], default='undetermined')
    history_ids = fields.One2many('hms.history', 'patient_id')

    _sql_constraints = [
        ('unique_email', 'UNIQUE("email")', 'Email Already Exist')
    ]

    @api.depends('birthdate')
    def calc_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = datetime.now().year - rec.birthdate.year
            else:
                rec.age = 0

    def create_log(self, state):
        self.env['hms.history'].create({
            'patient_id': self.id,
            'description': f'state changed to {state}',
        })

    def set_to_undetermined(self):
        self.state = 'undetermined'
        self.create_log('undetermined')

    def set_to_good(self):
        self.state = 'good'
        self.create_log('good')

    def set_to_fair(self):
        self.state = 'fair'
        self.create_log('fair')

    def set_to_serious(self):
        self.state = 'serious'
        self.create_log('serious')

    @api.onchange('age')
    def checked_pcr(self):
        for rec in self:
            if rec.age:
                if rec.age < 30:
                    rec.pcr = True
                    return {
                        'warning': {
                            'title': 'PCR',
                            'message': 'Pcr has been changed'
                        }
                    }

    @api.constrains('email')
    def check_email(self):
        for rec in self:
            if '@' not in rec.email:
                raise ValidationError("PLease insert a Valid Email")


class LogHistory(models.Model):
    _name = 'hms.history'

    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')






