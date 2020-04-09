from odoo import fields, models


class MembershipOffer(models.Model):
  _name = 'membership.offer'
  _description = 'Membership offer'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  name = fields.Char(string="Nom", required=1)
  membership_provider_id = fields.Many2one(string="Fournisseur d'adhésion", comodel_name='res.partner', domain=[('is_membership_provider', '=', True)])
  active = fields.Boolean(string="Actif", default=True)
  membership_offer_line_ids = fields.One2many(string="Lignes d'offre", comodel_name='membership.offer.line', inverse_name='membership_offer_id')
  sequence = fields.Integer(string="Séquence")
  subscriptable = fields.Boolean(string="Souscrivable ?")
  list_price_ids = fields.Many2many(string="Listes d eprix", comodel_name='product.pricelist')
  internal_ref = fields.Char(string="Référence interne")
