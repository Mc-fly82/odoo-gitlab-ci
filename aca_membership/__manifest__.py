{
  'name': 'Aca Membership',
  'version': '0.1',
  'category': 'Sudokeys',
  'sequence': 1,
  'summary': 'Automobile Club Association',
  'description': """Add membership model for ACA""",
  'author': 'Sudokeys',
  'website': 'http://www.sudokeys.com',
  'depends': [
    'base',
    'mail',
    'sale',
    'helpdesk',
    'contacts',
    'partner_contact_birthdate',
    'partner_contact_gender',
    'partner_firstname',
  ],
  'data': [
    'views/membership_menu.xml',
    # Security
    'security/res_group.xml',
    'security/ir.model.access.csv',
    # Views
    'views/membership_views.xml',
    'views/membership_offer_views.xml',
    'views/service_followup.xml',
    'views/res_partner.xml',
  ],
  'demo': [],
  'test': [],
  'init': [],
  'installable': True,
  'auto_install': False,
  'application': True,
}