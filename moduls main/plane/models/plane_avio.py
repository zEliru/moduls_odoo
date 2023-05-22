from odoo import models, fields
class plane_avio(models.Model):
        _name = 'plane.avio'
        name = fields.Char(compute='_get_name',string ="Avió ", readonly = 'True',store=False )
        codi = fields.Integer('Codi')
        imatge = fields.Binary('Imatge') # imatge o binary sus
        marca = fields.Integer('Marca')
        model = fields.Char('Model')
        maxVel = fields.Float('Velocitat màxima')

        def _get_name(self):
                for record in self:
                        record.name = str(record.codi)

