from odoo import models, fields
class plane_vol(models.Model):
        _name = 'plane.vol'
        codi = fields.Integer('Codi de vol')
        passatgers = fields.Integer('Número de passatgers')
        dataSortida = fields.DateTime('Data de sortida')
        dataArribada = fields.DateTime('Data d''arribada')



        