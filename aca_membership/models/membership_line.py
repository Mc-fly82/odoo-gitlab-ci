from odoo import fields, models, api, _

DISPLAY_TYPE = [
  ('standard', _("Standard")),
  ('line_section', _("Section")),
]


class MembershipLine(models.Model):
  _name = 'membership.line'

  product_id = fields.Many2one(string="Service", comodel_name="product.product", required=1, domain=[('type', '=', 'service')])
  membership_id = fields.Many2one(string="Adhésion", comodel_name='membership')
  option = fields.Boolean(string="Option", required=1)
  max_qty = fields.Integer(string="Quantité max", required=1)
  sequence = fields.Integer(string="Séquence")
  consumed_qty = fields.Integer(string="Quantité consommée", compute='_compute_consumed_qty')
  reamining_qty = fields.Integer(string="Quantité restante", compute='_compute_remaining_qty')
  display_type = fields.Selection(selection=DISPLAY_TYPE, default='standard', required=1)

  # @api.onchange('consumed_qty', 'max_qty')
  # def _compute_remaining_qty(self):
  #   for line in self:
  #     line.reamining_qty = line.max_qty - line.consumed_qty

  # @api.multi
  # def _compute_consumed_qty(self):
  #   for line in self:
  #     line.consumed_qty = 0
