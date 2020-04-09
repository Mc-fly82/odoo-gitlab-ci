from odoo import fields, models


class CarRegistration(models.Model):
  _name = 'car.registration'

  name = fields.Char(string="Nom véhicule")
  matriculation = fields.Char(string="Immatriculation")
  registration_card = fields.Char(string="Carte grise")
  owner_id = fields.Many2one(string="Propriétaire", comodel_name='res.partner')
