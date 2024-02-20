from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InheritCrm(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    @api.model
    def create(self, vals):
        if vals['email'] == self.related_patient_id.email:
                raise ValidationError('Email must be unique')
        return super().create(vals)

    def unlink(self):
        for rec in self:
            if rec.related_patient_id == False:
                super().unlink()
            else:
                raise ValidationError('cannot Delete a patient user')









