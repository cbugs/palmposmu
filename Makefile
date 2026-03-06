up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

# Website commands
www-install:
	cd www && npm install

www-dev:
	cd www && npm run dev

www-build:
	cd www && npm run build

www-preview:
	cd www && npm run preview

# Build and deploy website
deploy-www: 
	www-build
	docker compose up -d palmpos_www

# Setup everything
setup: www-install
	@echo "Setup complete! Run 'make www-build' to build the website, then 'make up' to start all services."

.PHONY: create-site
create-site:
	docker exec -i palmpos_app bash -c "odoo -d palmpos_$(SUBDOMAIN) -i base,point_of_sale,muk_web_appsbar,muk_web_chatter,muk_web_colors,muk_web_dialog,muk_web_group,muk_web_refresh,muk_web_theme,palmpos_contact,palmpos_theme,palmpos_title,pos_auto_redirect,pos_screensaver,pos_receipt_customize,palmpos_profit_report,web_replace_url --without-demo=all --stop-after-init"
	
#odoo -d palmpos_demo -i base --db_host=host.docker.internal --db_port=5432 --db_user=palmpos --db_password=palmpos --stop-after-init

#odoo -d palmpos_demo -i base,pos --without-demo=all --stop-after-init

build-www:
	docker run --rm -v $(shell pwd)/www:/app -w /app node:18 sh -c "npm install && npm run build"

# Load environment variables from .env file
include .env
export

# Database backup using pg_dump (requires DB parameter, reads credentials from .env)
# Usage: make backup DB=palmpos
.PHONY: backup
backup:
	@bash backup-db.sh $(DB) $(POSTGRES_USER) $(POSTGRES_PASSWORD) localhost 5432

# Update module in specific database
# Usage: make update-module DB=palmpos_demo MODULE=palmpos_theme
.PHONY: update-module
update-module:
	docker exec -it palmpos_app odoo -d $(DB) -u $(MODULE) --stop-after-init

# Update module across all configured databases
# Usage: make update-module-all MODULE=palmpos_theme
.PHONY: update-module-all
update-module-all:
	@bash update-module.sh $(MODULE)