{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Gestion de livres avec ventes et achats',
    'description': 'Module pour gérer les livres d’une bibliothèque, ventes et achats.',
    'category': 'Sales',
    'author': 'Robin Mvukulu',
    'depends': ['base', 'sale', 'purchase', 'product'],
    'data': [
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}
