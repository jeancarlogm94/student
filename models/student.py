# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student (models.Model):
    _name = "student.student"
    _descrpiption = "Datos del Estudiante"

    codigo = fields.Char(copy=False, default='New', readonly=True)
    nombre = fields.Char(string='Nombre')
    primer_apellido = fields.Char(string='Primer Apellido')
    segundo_apellido = fields.Char(string='Segundo Apellido', )
    edad = fields.Integer(string='Edad')
    sexo = fields.Selection(
        selection=[('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Sexo')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    hobby = fields.Char(string="Hobby")
    direccion = fields.Char(string="Dirección")
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    acudiente = fields.Char(string='Acudiente')

    @api.model
    def create(self, vals):
        if vals.get('codigo', 'New') == 'New':
            vals['codigo'] = self.env['ir.sequence'] or 'New'

        result = super(Student, self).create(vals)
        return result
