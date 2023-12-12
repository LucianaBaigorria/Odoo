from odoo import models, fields  #librerias importadas desde odoo

#creamos un modelo(tabla de la base de datos) a partir de una clase
class Alumno(models.Model):
    _name = 'alumno'  #nombre de la tabla que se va a crear

    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nro_legajo = fields.Char(string='Nro de Legajo')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Char(string='Dirección')
    pais = fields.Many2one('res.country', string='País')

#atributos
#_name para crear un nuevo modelo
#_inherit para heredar de un modelo que ya existe en odoo