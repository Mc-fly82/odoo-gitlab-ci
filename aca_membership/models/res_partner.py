from odoo import fields, models, api


class ResPartner(models.Model):
  _inherit = 'res.partner'

  is_membership_provider = fields.Boolean(string="Est un fournisseur d'adhésion ?")
  direct_membership = fields.Boolean(string="Adhérent direct", default=True)
  membership_provider_id = fields.Many2one(string="Fournisseur d'ashésion", comodel_name='res.partner')
  membership_ids = fields.One2many(string="Adhésions", comodel_name='membership', inverse_name='member_id')
  phone_office = fields.Char(string="Téléphone bureau")
  job = fields.Char(string="Profession")
  godparent = fields.Many2one(string="Parrain", comodel_name='res.partner')
  godson = fields.One2many(string="Filleul", comodel_name='res.partner', inverse_name='godparent')
  dateadh = fields.Date(string="Date d'adhésion", compute='_compute_first_membership_date')
  vehicule_ids = fields.One2many(string="Véhicules", comodel_name='car.registration', inverse_name='owner_id')
  npai = fields.Boolean(string="NPAI", help="N'habite pas à l'adresse indiqué")
  emergency_email = fields.Char(string="Email de secours")
  wrong_email = fields.Boolean(string="Email faux ?", help="Saisi manuel")

  @api.depends('membership_ids')
  def _compute_first_membership_date(self):
    # TODO: finish me
    for partner in self:
      return False
