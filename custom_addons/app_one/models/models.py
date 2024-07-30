# -*- coding: utf-8 -*-

from odoo import models, fields, api

# model for property attributes
class Property(models.Model):
	_name = "property"
	_description ="property"

	name = fields.Char()
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date()
	expected_price = fields.Float()
	selling_price = fields.Float()
	expected_price = fields.Float()
	bed_rooms = fields.Integer()
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection([
		('north','North'),
		('south','South'),
		('east','East'),
		('west','West')])





#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
