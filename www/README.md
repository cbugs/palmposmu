# PalmPOS Website

Modern website for PalmPOS built with Vite, Vue 3, and Tailwind CSS.

## Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Deployment

The website is automatically deployed via Docker using nginx.

Build the production files:
```bash
npm run build
```

Start the containers:
```bash
docker compose up -d
```

The website will be available at http://localhost:8080

## Features

- Modern, responsive design
- Vue Router for navigation
- Tailwind CSS for styling
- Optimized production builds
- SEO friendly
