{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Gestion de livres : achat, vente et suivi des exemplaires',
    'description': 'Entrainement: Module pour gérer les livres d’une bibliothèque, achats, ventes et stock.',
    'category': 'Sales',
    'author': 'Robin Mvukulu',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}
