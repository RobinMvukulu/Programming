from odoo import models, fields, api
from datetime import date

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"
    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    published_date = fields.Date(string="Published Date")
    isbn = fields.Char(string="ISBN", required=True, unique=True)

    age_of_book = fields.Integer(
        string="Age of Book",
        compute="_compute_age_of_book",
        store=True
    )

    _sql_constraints = [
        ("isbn_unique", "unique(isbn)", "The ISBN must be unique!")
    ]

    @api.depends("published_date")
    def _compute_age_of_book(self):
        for book in self:
            if book.published_date:
                book.age_of_book = date.today().year - book.published_date.year
            else:
                book.age_of_book = 0
