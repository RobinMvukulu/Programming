from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livre'

    name = fields.Char(string='Titre', required=True)
    author = fields.Char(string='Auteur')
    isbn = fields.Char(string='ISBN')
    price = fields.Float(string='Prix')
    copies_available = fields.Integer(string='Exemplaires disponibles', default=0)

    purchase_ids = fields.One2many('purchase.order.line', 'product_id', string='Achats')
    sale_ids = fields.One2many('sale.order.line', 'product_id', string='Ventes')
