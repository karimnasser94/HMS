from odoo import models, fields


class InheritCrm(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')
