from odoo import fields, models, _

STATE = [
  ("active", _("Actif")),
  ("inactive", _("Inactif")),
  ("unknow", _("Inconnu")),
  ("renew", _("Renouvellement"))
]


class Membership(models.Model):
  _name = 'membership'
  _sql_constraints = [('provider_unique_charseq', 'unique (provider_unique_charseq)', _("Id already exist !"))]
  _inherit = ['mail.thread', 'mail.activity.mixin']

  date_start = fields.Date(string="Date de début")
  date_end = fields.Date(string="Date de fin")
  member_id = fields.Many2one(string="Adhérent", comodel_name='res.partner')
  membership_provider = fields.Char(string="Fournisseur d'adhésion", related="offer_id.membership_provider_id.name", readonly=1)
  name = fields.Char(string="Nom", required=1)
  offer_id = fields.Many2one(string="Offre", comodel_name='membership.offer')
  provider_unique_charseq = fields.Char(string="Identifiant", required=1)
  # renew_id = fields.Many2one(string="Renew", comodel_name='membership.renew')
  service_ids = fields.One2many(string="Services", comodel_name='membership.line', inverse_name="membership_id")
  state = fields.Selection(string="État", selection=STATE, track_visibility='onchange')
