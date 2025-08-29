from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    author = fields.Char('Author')
    isbn = fields.Char('ISBN')
    price = fields.Float('Price')
    product_id = fields.Many2one('product.product', string='Related Product', domain="[('type','=','product')]")
    copies_available = fields.Integer('Copies Available', related='product_id.qty_available', store=True)

    def create_product_for_book(self):
        """Create a product for each book if not already linked."""
        for book in self:
            if not book.product_id:
                product = self.env['product.product'].create({
                    'name': book.name,
                    'list_price': book.price,
                    'type': 'product',
                })
                book.product_id = product
