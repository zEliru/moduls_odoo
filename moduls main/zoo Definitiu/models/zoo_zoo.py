from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    grandaria = fields.Float('Grandària')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Nom de la ciutat')
    pais = fields.Char('Pais')

    