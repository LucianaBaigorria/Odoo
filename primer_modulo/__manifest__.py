# -*- coding: utf-8 -*-
{
    "name": "Modulo_alumno",
    'summary': """
    modulos de inscripcion y programas de alumnos
    """,
    'author': "luciana",
    'category': 'educacion',
    'version': '1.0',
    'depends':[],
    'data':[
        'views/alumno_view.xml',
        'views/inscripcion_view.xml',
        'views/programa_view.xml',
        'security/ir.model.access.csv'
    ],
}

#En el manifest se declaran todas las librerias, data, vistas para que el modulo funcione