# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /opt/odoo15/addons/custom/tutorials_tasks/school(models.Model):
#     _name = '/opt/odoo15/addons/custom/tutorials_tasks/school./opt/odoo15/addons/custom/tutorials_tasks/school'
#     _description = '/opt/odoo15/addons/custom/tutorials_tasks/school./opt/odoo15/addons/custom/tutorials_tasks/school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100