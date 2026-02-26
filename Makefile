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
	docker exec -i palmpos_app bash -c "odoo -d palmpos_$(SUBDOMAIN) -i base,point_of_sale --without-demo=all --stop-after-init"
	
#odoo -d palmpos_demo -i base --db_host=host.docker.internal --db_port=5432 --db_user=palmpos --db_password=palmpos --stop-after-init

#odoo -d palmpos_demo -i base,pos --without-demo=all --stop-after-init

build-www:
	docker run --rm -v $(shell pwd)/www:/app -w /app node:18 sh -c "npm install && npm run build"