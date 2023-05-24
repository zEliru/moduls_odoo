from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name',string ="Espècie ", readonly = 'True',store=False )
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom científic')
    nomvulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')
    animal_ids = fields.One2many('zoo.animal','especie_id', string='Animal IDs')

    def _get_name(self):
        for record in self:
            record.name = str(record.id) +  ": " + str(record.nomvulgar)