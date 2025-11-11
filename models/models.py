# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class hfc_project_cost_aggregator(models.Model):
#     _name = 'hfc_project_cost_aggregator.hfc_project_cost_aggregator'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100