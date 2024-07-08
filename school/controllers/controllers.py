# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo15/addons/custom/tutorialsTasks/school(http.Controller):
#     @http.route('//opt/odoo15/addons/custom/tutorials_tasks/school//opt/odoo15/addons/custom/tutorials_tasks/school', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo15/addons/custom/tutorials_tasks/school//opt/odoo15/addons/custom/tutorials_tasks/school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo15/addons/custom/tutorials_tasks/school.listing', {
#             'root': '//opt/odoo15/addons/custom/tutorials_tasks/school//opt/odoo15/addons/custom/tutorials_tasks/school',
#             'objects': http.request.env['/opt/odoo15/addons/custom/tutorials_tasks/school./opt/odoo15/addons/custom/tutorials_tasks/school'].search([]),
#         })

#     @http.route('//opt/odoo15/addons/custom/tutorials_tasks/school//opt/odoo15/addons/custom/tutorials_tasks/school/objects/<model("/opt/odoo15/addons/custom/tutorials_tasks/school./opt/odoo15/addons/custom/tutorials_tasks/school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo15/addons/custom/tutorials_tasks/school.object', {
#             'object': obj
#         })
