from odoo import fields, models, _

DISPLAY_TYPE = [
  ('standard', _("Standard")),
  ('line_section', _("Section")),
]


class MembershipOfferLine(models.Model):
  _name = 'membership.offer.line'

  membership_offer_id = fields.Many2one(string="Offre", comodel_name='membership.offer', required=1)
  option = fields.Boolean(string="Optionnel ?", required=1)
  max_qty = fields.Integer(string="Quantité max", required=1)
  sequence = fields.Integer(string="Séquence")
  product_id = fields.Many2one(string="Article", comodel_name='product.product', required=1)
  display_type = fields.Selection(selection=DISPLAY_TYPE, default='standard', required=1)
  internal_ref = fields.Char(string="Référence interne")
  infinite_product = fields.Boolean(string="Illimité ?")
  active = fields.Boolean(string="Actif", default=True)
