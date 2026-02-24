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
deploy-www: www-build
	docker compose up -d palmpos_www

# Setup everything
setup: www-install
	@echo "Setup complete! Run 'make www-build' to build the website, then 'make up' to start all services."