from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentorigen = fields.Char('Continent origen')
    datanaix = fields.Char('Data de naixament')
    paisorigen = fields.Char('Pais origen')
    sexe = fields.Char('Sexe')