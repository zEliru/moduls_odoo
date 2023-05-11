from odoo import models, fields
class plane_aeroport(models.Model):
        _name = 'plane.aeroport'
        codi = fields.Integer('Codi')
        nom = fields.Char('Nom de l''aeroport')
        imatge = fields.Char('Imatge')
        ciutat = fields.Char('Ciutat')
        pais = fields.Char('Païs')
        latitud = fields.Float('Coord 1')
        longitud = fields.Float('Coord 2')


        