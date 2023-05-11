from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentOrigen = fields.Char('Continent origen')
    dataNaix = fields.Date('Data de naixament')
    paisOrigen = fields.Char('Pais origen')
    sexe = fields.Char('Sexe')
    