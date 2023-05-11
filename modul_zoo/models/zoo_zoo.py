from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.zoo'
    grandaria = fields.Integer('Grandària')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Nom de la ciutat')
    Pais = fields.Char('Pais')

    