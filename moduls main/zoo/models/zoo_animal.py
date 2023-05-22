from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    name = fields.Char(compute='_get_name',string ="Animal ", readonly = 'True',store=False )
    continentorigen = fields.Char('Continent origen')
    datanaix = fields.Date('Data de naixament')
    paisorigen = fields.Char('Pais origen')
    sexe = fields.Char('Sexe')
    zoo_id = fields.Many2one('zoo.zoo','Zoo')
    especie_id = fields.Many2one('zoo.especie',string='Espècie')
    def _get_name(self):
        for record in self:
            record.name = "Animal id: " + str(record.id)