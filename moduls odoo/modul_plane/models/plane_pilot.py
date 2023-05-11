from odoo import models, fields
class plane_pilot(models.Model):
        _name = 'plane.pilot'
        codi = fields.Integer('Codi pilot')
        nom = fields.Char('Nom del pilot')
        cognoms = fields.Char('Cognoms del pilot')
        nif = fields.Char('NIF')
        telf = fields.Char('Telèfon')
        email = fields.Char('Email')

        