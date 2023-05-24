from odoo import models, fields
class plane_pilot(models.Model):
        _name = 'plane.pilot'
        name = fields.Char(compute='_get_name',string ="Pilot ", readonly = 'True',store=False )
        codi = fields.Integer('Codi pilot')
        nom = fields.Char('Nom del pilot')
        cognoms = fields.Char('Cognoms del pilot')
        nif = fields.Char('NIF')
        telf = fields.Char('Telèfon')
        email = fields.Char('Email')
        vol_ids = fields.One2many('plane.vol','pilot_id',string='vols')

        def _get_name(self):
                for record in self:
                        record.name = str(record.nom) +  " " + str(record.cognoms)

        