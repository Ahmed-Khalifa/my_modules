# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\a.alhadi\odoo\myModules\reportsmodule(http.Controller):
#     @http.route('/c:\users\a.alhadi\odoo\my_modules\reportsmodule/c:\users\a.alhadi\odoo\my_modules\reportsmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\a.alhadi\odoo\my_modules\reportsmodule/c:\users\a.alhadi\odoo\my_modules\reportsmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\a.alhadi\odoo\my_modules\reportsmodule.listing', {
#             'root': '/c:\users\a.alhadi\odoo\my_modules\reportsmodule/c:\users\a.alhadi\odoo\my_modules\reportsmodule',
#             'objects': http.request.env['c:\users\a.alhadi\odoo\my_modules\reportsmodule.c:\users\a.alhadi\odoo\my_modules\reportsmodule'].search([]),
#         })

#     @http.route('/c:\users\a.alhadi\odoo\my_modules\reportsmodule/c:\users\a.alhadi\odoo\my_modules\reportsmodule/objects/<model("c:\users\a.alhadi\odoo\my_modules\reportsmodule.c:\users\a.alhadi\odoo\my_modules\reportsmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\a.alhadi\odoo\my_modules\reportsmodule.object', {
#             'object': obj
#         })
