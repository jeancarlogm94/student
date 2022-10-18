# -*- coding: utf-8 -*-
{
    'name': "Estudiantes",
    'description': """
        Aplicacion para la gestion de los estudiantes
    """,
    'author': "jeancarlogm94",
    'website': "https://jgd-portfolio.vercel.app/",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
