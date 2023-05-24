from odoo import models, fields
class plane_aeroport(models.Model):
        _name = 'plane.aeroport'
        name = fields.Char(compute='_get_name',string ="Aeroport ", readonly = 'True',store=False )
        codi = fields.Integer('Codi')
        nom = fields.Char('Nom de l''aeroport')
        imatge = fields.Binary('Imatge') #char o binary o imatge?? idk
        ciutat = fields.Char('Ciutat')
        pais = fields.Char('Païs')
        latitud = fields.Float('Coord 1')
        longitud = fields.Float('Coord 2')
        vol_ids = fields.One2many('plane.vol','aeroport_id',string='Aeroport de sortida')
        vol_ids_2 = fields.One2many('plane.vol','aeroport_id_2',string='Aeroport d arribada')


        def _get_name(self):
                for record in self:
                        record.name = str(record.codi) +  ": " + str(record.nom)

