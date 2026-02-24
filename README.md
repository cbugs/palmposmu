# PalmPOS Project

Complete PalmPOS system with Odoo backend and modern marketing website.

## Project Structure

```
palmpos/
├── app/                    # Odoo application
│   ├── addons/            # Custom Odoo addons
│   ├── config/            # Odoo configuration
│   │   └── odoo.conf     # Main Odoo config (includes Brevo SMTP)
│   ├── .env              # Environment variables
│   └── .env.example      # Example environment file
├── www/                   # Marketing website (Vue 3 + Vite + Tailwind)
│   ├── src/              # Source files
│   │   ├── components/   # Vue components
│   │   ├── views/        # Page views
│   │   ├── App.vue       # Main app component
│   │   ├── main.js       # Application entry
│   │   └── style.css     # Global styles
│   ├── public/           # Static assets
│   ├── dist/             # Production build (generated)
│   ├── nginx.conf        # Nginx configuration
│   └── package.json      # Node dependencies
├── docker-compose.yml     # Docker services configuration
├── Makefile              # Build and run commands
└── README.md             # This file
```

## Services

### Odoo POS System
- **Port**: 8070
- **URL**: http://localhost:8070
- **Demo Login**: 
  - Username: `demo`
  - Password: `password`

### PalmPOS Website
- **Port**: 8080
- **URL**: http://localhost:8080
- **Technology**: Vue 3 + Vite + Tailwind CSS
- **Features**:
  - Modern responsive design
  - Full feature showcase
  - Pricing information
  - Privacy & Terms pages
  - Contact form
  - Direct link to Odoo demo

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js (for website development)
- Make (optional, for convenience commands)

### Setup

1. **Install website dependencies**:
```bash
make www-install
# or manually:
cd www && npm install
```

2. **Build the website**:
```bash
make www-build
# or manually:
cd www && npm run build
```

3. **Start all services**:
```bash
make up
# or manually:
docker compose up -d
```

4. **Access the applications**:
- Website: http://localhost:8080
- Odoo: http://localhost:8070

## Makefile Commands

### Docker Commands
- `make up` - Start all services
- `make down` - Stop all services
- `make restart` - Restart all services

### Website Commands
- `make www-install` - Install dependencies
- `make www-dev` - Start development server
- `make www-build` - Build for production
- `make www-preview` - Preview production build
- `make deploy-www` - Build and deploy website

### Setup
- `make setup` - Initial setup (install dependencies)

## Development

### Website Development

Start the development server with hot reload:
```bash
make www-dev
# or
cd www && npm run dev
```

The dev server will run on http://localhost:5173

### Odoo Development

1. Place custom addons in `app/addons/`
2. Update `app/config/odoo.conf` as needed
3. Restart the service:
```bash
make restart
```

## Configuration

### Odoo Configuration

Edit `app/config/odoo.conf` to configure:
- Database settings
- SMTP settings (currently configured for Brevo)
- Admin password
- Other Odoo options

### Environment Variables

Copy `app/.env.example` to `app/.env` and configure:
- Database credentials
- Other environment-specific settings

### Brevo Email Configuration

The Odoo system is configured to use Brevo (Sendinblue) for email:
- SMTP Server: smtp-relay.brevo.com
- Port: 587 (STARTTLS)

Update the following in `app/config/odoo.conf`:
- `smtp_user` - Your Brevo login email
- `smtp_password` - Your Brevo SMTP key
- `email_from` - Your verified sender email

## Website Features

### Pages
- **Home** - Hero section, feature overview, stats, CTA
- **Features** - Detailed feature descriptions with categories
- **Pricing** - Pricing tiers and FAQ
- **About** - Company information and values
- **Contact** - Contact form and business information
- **Privacy** - Privacy policy
- **Terms** - Terms of service

### Design Features
- Responsive design (mobile-first)
- Smooth animations and transitions
- Modern gradient backgrounds
- Optimized performance
- SEO friendly
- Accessible

### Technology Stack
- Vue 3 (Composition API)
- Vite (Build tool)
- Vue Router (SPA routing)
- Tailwind CSS (Styling)
- Nginx (Production server)

## Deployment

### Production Build

1. Build the website:
```bash
make www-build
```

2. Deploy with Docker:
```bash
make up
```

The website will be served by Nginx on port 8080.

### Custom Domain

To use a custom domain:
1. Update `www/nginx.conf` with your domain
2. Configure DNS to point to your server
3. Add SSL certificate configuration to nginx
4. Rebuild and restart:
```bash
make deploy-www
```

## Troubleshooting

### Website not loading
- Check if nginx container is running: `docker ps`
- Check if build files exist: `ls www/dist`
- Rebuild: `make www-build && make up`

### Odoo not starting
- Check logs: `docker logs odoo_web`
- Verify `.env` file exists and is configured
- Check port 8070 is not already in use

### Build errors
- Clear node_modules: `cd www && rm -rf node_modules && npm install`
- Clear build cache: `cd www && rm -rf dist`

## License

Copyright © 2026 Palmtree Mauritius. All rights reserved.
