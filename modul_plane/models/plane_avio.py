from odoo import models, fields
class plane_avio(models.Model):
        _name = 'plane.avio'
        codi = fields.Integer('Codi')
        imatge = fields.Char('Imatge') # imatge o binary sus
        marca = fields.Integer('Marca')
        model = fields.Char('Model')
        maxVel = fields.Float('Velocitat màxima')
        
