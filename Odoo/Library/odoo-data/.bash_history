odoo -i base --db_host=db --db_user=odoo --db_password=odoo
cls
docker compose run --rm odoo -i base --stop-after-init
\q
exit
psql -h db -U odoo -d odoo
exit
