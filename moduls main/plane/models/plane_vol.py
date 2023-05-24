from odoo import models, fields
class plane_vol(models.Model):
        _name = 'plane.vol'
        name = fields.Char(compute='_get_name',string ="Nom complet", readonly = 'True',store=False )
        codi = fields.Integer('Codi de vol')
        passatgers = fields.Integer('Número de passatgers')
        dataSortida = fields.Datetime('Data de sortida')
        dataArribada = fields.Datetime('Data d''arribada')
        aeroport_id = fields.Many2one('plane.aeroport','Aeroport sortida')
        aeroport_id_2 = fields.Many2one('plane.aeroport','Aeroport arribada')
        pilot_id = fields.Many2one('plane.pilot',string='Pilot')
        plane_id = fields.Many2one('plane.avio','Avió')

        def _get_name(self):
                for record in self:
                        record.name = str(record.codi)
        




        