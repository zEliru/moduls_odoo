﻿from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom científic')
    nomvulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')