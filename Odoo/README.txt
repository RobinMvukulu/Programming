Commandes:

Environnement virtuel: .\venv\Scripts\activate
Serveur Odoo: python odoo-bin -c ..\odoo.conf
Master password: ptj4-3q2u-ckxb


depends=['base'] - Module cœur d’Odoo pour définir utilisateurs, entreprises...
sql_constraints - Règles au niveau de PostgreSQL pour garantir l’unicité des données par exemple.
@api.constrains - 
Port 8069 = port HTTP d’Odoo
Port 5432 = port PostgreSQL