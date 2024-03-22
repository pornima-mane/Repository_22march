from odoo import SUPERUSER_ID
from odoo import models, fields, api


class wizard_vendor(models.TransientModel):
    _name = "wizard_vendor"
    _description = "Customer Credit Limit"
    # _inherit = "sale.order"
    # _inherit = "mail.compose.message"


    vendors = fields.Many2many('res.partner',string="Vendors", domain="['|', ('company_id', '=', False), ('company_id', '=', company_id),('partner_type','=','supplier')]",
                                 )
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company.id)

    def confirm_sale(self):
        req_id = self.env['purchase.request.order'].sudo().browse(self._context.get('active_ids'))
        for ven in self.vendors:
            rfq_vals = {
                'date_order': req_id.date_order,
                'currency_id': req_id.currency_id.id,
                'date_planned': req_id.date_planned,
                'user_id': req_id.user_id.id,
                'company_id': req_id.company_id.id,
                'payment_term_id': req_id.payment_term_id.id,
                'fiscal_position_id': req_id.fiscal_position_id.id,
                'request_id': req_id.id,
                'partner_id': ven.id,
            }
            rfq = self.env['purchase.rfq'].create(rfq_vals)
            for line in req_id.order_line:
                order_line_vals = {
                    # 'purchase_request_line_id': line.id,
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'quantity': line.quantity,
                    'product_uom': line.product_uom.id,
                    # 'product_packaging_qty': line.product_packaging_qty,
                    # 'product_packaging_id': line.product_packaging_id.id,
                    'price_unit': line.price_unit,
                    'taxes_id': [(6, 0, line.taxes_id.ids)],
                    'order_id': rfq.id
                }
                self.env['purchase.rfq.line'].create(order_line_vals)
                # rfq_vals['order_line'].append((0, 0, order_line_vals))

        action = {
            'type': 'ir.actions.act_window',
            'name': 'Create RFQ',
            'res_model': 'purchase.rfq',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('request_id','=',req_id.id)]

        }
        return action

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
