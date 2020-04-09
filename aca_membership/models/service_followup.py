from odoo import models, fields, _

STATE = [
  ('draft', _("Demande")),
  ('awaiting', _("En attente")),
  ('valid', _("Validé")),
  ('done', _("Terminé")),
]


class ServiceFollowup(models.Model):
  _name = 'service.followup'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  request_date = fields.Date(string="Date de demande", required=1)
  service_consumption_date = fields.Date(string="Date de consommation")
  member_id = fields.Many2one(string="Adhérent", comodel_name='res.partner')
  product_id = fields.Many2one(string="Article", comodel_name='product.product')
  state = fields.Selection(string="État", selection=STATE, default='draft', track_visibility='onchange')
  order_id = fields.Many2one(string="Bon de commande", comodel_name='sale.order')
  ticket_id = fields.Many2one(string="Ticket", comodel_name='helpdesk.ticket')
