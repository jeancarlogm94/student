# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = "student.student"
    nombre = fields.Char(string='Nombre')
    primer_apellido = fields.Char(string='Primer Apellido')
    segundo_apellido = fields.Char(string='Segundo Apellido', )
    edad = fields.Integer(string='Edad')
    sexo = fields.Selection(
        selection=[('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Sexo')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    hobby = fields.Char(string="Hobby")
    direccion = fields.Char(string="Dirección")
    ciudad = fields.Many2one('res.city', string='Ciudad')
    acudiente = fields.Char(string='Acudiente')
