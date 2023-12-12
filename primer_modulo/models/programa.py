from odoo import models, fields, api

class Programa(models.Model):
    _name = 'programa'


    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')


@api.model
def get_alumnos_inscritos(self):
    alumnos = []
    inscripciones = self.env['mi_modulo.inscripcion'].search([('programa_id', '=', self.id)])
    for inscripcion in inscripciones:
        alumno_data = {
            'nombre': inscripcion.alumno.nombre,
            'apellido': inscripcion.alumno.apellido,
            'legajo': inscripcion.alumno.nro_legajo,
            'fecha_nacimiento': inscripcion.alumno.fecha_nacimiento,
            'email': inscripcion.alumno.email,
            'telefono': inscripcion.alumno.telefono,
            'pais': {
                'id': inscripcion.alumno.pais.id,
                'nombre': inscripcion.alumno.pais.name,
            }
        }
        alumnos.append(alumno_data)
    return alumnos