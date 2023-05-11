from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom científic')
    nomVulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')

    