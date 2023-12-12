from odoo import models, fields, api

class Inscripcion(models.Model):
    _name = 'inscripcion'


    alumno = fields.Many2one('alumno', string='Alumno')
    programa = fields.Many2one('programa', string='Programa')