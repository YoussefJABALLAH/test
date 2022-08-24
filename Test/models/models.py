# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

     @api.onchange("product_id")
      def check_product(self):
        if self.product_id:
            product_ex = self.search([('product_id', '=', self.product_id)])
            if product_ex:
                return {
                    'warning': {
                        'title': _("Avertissement"),
                        'message': _("Vous avez ajouté l’article … en double")
                     }
                 }
