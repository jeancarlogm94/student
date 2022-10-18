# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class Student (models.Model):
    _name = "student.student"
    _descrpiption = "Datos del Estudiante"

    codigo = fields.Char(copy=False, default='0', readonly=True)
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    edad = fields.Integer(string='Edad')
    sexo = fields.Selection(
        selection=[('m', 'Masculino'), ('f', 'Femenino')], string='Sexo')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    hobby = fields.Char(string="Hobby")
    direccion = fields.Char(string="Dirección")
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    acudiente = fields.Char(string='Acudiente')

    @api.model
    def create(self, vals):
        if vals.get('codigo', '0') == '0':
            vals['codigo'] = self.env['ir.sequence'].next_by_code(
                'student.student.id') or '0'

        result = super(Student, self).create(vals)
        return result
