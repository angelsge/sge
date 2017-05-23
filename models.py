#-*- coding: utf-8 -*-
from openerp import models, fields

class citasaldg_citas(models.Model):
    _name = 'citas.cita'
    autor = fields.Char('Autor', required=True, help='Introduzca el autor.')
    cita = fields.Text('Cita', required=True, help='Introduzca la cita')
    fecha = fields.Date('Fecha', help='Introduzca la fecha de visualización.')
    orden = fields.Integer('Orden', help='Introduzca el orden de aparación')