from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    name = fields.Char(compute='_get_name',string ="Zoo ", readonly = 'True',store=False )
    grandaria = fields.Float('Grandària')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Nom de la ciutat')
    pais = fields.Char('Pais')
    def _get_name(self):
        for record in self:
            record.name = str(record.nom)

    