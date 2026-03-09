#!/bin/bash

# Script to create a new site from template
# Prerequisites: chmod +x create-site.sh
# Usage: ./create-site.sh "Site Name" "site-slug"

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Error: Site name and slug are required"
    echo "Usage: ./create-site.sh \"Site Name\" \"site-slug\""
    echo "Example: ./create-site.sh \"Hungry Food\" \"hungry-food\""
    exit 1
fi

SITE_NAME=$1
SITE_SLUG=$2
DB_NAME="palmpos_${SITE_SLUG}"
TEMPLATE_DB="palmpos_template1"
CONFIG_FILE="databases.conf"
ENV_FILE=".env"

# Load database credentials from .env file
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: $ENV_FILE not found"
    exit 1
fi

# Read specific values from .env file without exporting globally
POSTGRES_USER=$(grep "^POSTGRES_USER=" "$ENV_FILE" | cut -d '=' -f2)
POSTGRES_PASSWORD=$(grep "^POSTGRES_PASSWORD=" "$ENV_FILE" | cut -d '=' -f2)

if [ -z "$POSTGRES_USER" ]; then
    echo "Error: POSTGRES_USER not found in $ENV_FILE"
    exit 1
fi

echo "==========================================="
echo "Creating new site"
echo "==========================================="
echo "Site Name: $SITE_NAME"
echo "Slug: $SITE_SLUG"
echo "Database: $DB_NAME"
echo "Template: $TEMPLATE_DB"
echo "==========================================="
echo ""

# Step 1: Terminate connections to template database
echo "Step 1: Disconnecting users from template database..."
PGPASSWORD="$POSTGRES_PASSWORD" psql -U "$POSTGRES_USER" -h localhost -d postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '$TEMPLATE_DB' AND pid <> pg_backend_pid();"

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Could not terminate all connections"
fi
echo "✓ Template database ready"
echo ""

# Step 2: Create database from template
echo "Step 2: Creating database from template..."
PGPASSWORD="$POSTGRES_PASSWORD" createdb "$DB_NAME" -T "$TEMPLATE_DB" -O "$POSTGRES_USER" -U "$POSTGRES_USER" -h localhost

if [ $? -ne 0 ]; then
    echo "✗ Failed to create database"
    exit 1
fi
echo "✓ Database created successfully"
echo ""

# Step 2.5: Copy filestore from template to new database
echo "Step 2.5: Copying filestore from template..."
# First remove any existing filestore for new DB
docker exec -u root palmpos_app rm -rf /var/lib/odoo/.local/share/Odoo/filestore/"$DB_NAME"
# Then copy the template filestore contents
docker exec -u root palmpos_app cp -r /var/lib/odoo/.local/share/Odoo/filestore/"$TEMPLATE_DB" /var/lib/odoo/.local/share/Odoo/filestore/"$DB_NAME"
# Fix ownership
docker exec -u root palmpos_app chown -R odoo:odoo /var/lib/odoo/.local/share/Odoo/filestore/"$DB_NAME"

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Could not copy filestore"
else
    echo "✓ Filestore copied successfully"
fi
echo ""

# Step 3: Update company name
echo "Step 3: Updating company name to '$SITE_NAME'..."
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "UPDATE res_company SET name = '$SITE_NAME' WHERE id = 1;"

if [ $? -ne 0 ]; then
    echo "✗ Failed to update company name"
    exit 1
fi
echo "✓ Company name updated"
echo ""

# Step 4: Update Point of Sale name
echo "Step 4: Updating Point of Sale name to '$SITE_NAME'..."
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "UPDATE pos_config SET name = '$SITE_NAME' WHERE id = 1;"

if [ $? -ne 0 ]; then
    echo "✗ Failed to update POS name"
    exit 1
fi
echo "✓ Point of Sale name updated"
echo ""

# Step 4.5: Regenerate asset bundles
echo "Step 4.5: Regenerating asset bundles..."
docker exec palmpos_app odoo shell -d "$DB_NAME" --db_host=host.docker.internal --db_user="$POSTGRES_USER" --db_password="$POSTGRES_PASSWORD" <<EOF
self.env['ir.attachment'].regenerate_assets_bundles()
self.env.cr.commit()
exit()
EOF

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Could not regenerate assets"
else
    echo "✓ Asset bundles regenerated"
fi
echo ""

# Step 5: Add to databases.conf
echo "Step 5: Adding to $CONFIG_FILE..."
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Warning: $CONFIG_FILE not found, creating it"
    echo "# List of databases for update-module.sh" > "$CONFIG_FILE"
    echo "# One database name per line" >> "$CONFIG_FILE"
    echo "" >> "$CONFIG_FILE"
fi

# Check if database already exists in config
if grep -q "^${DB_NAME}$" "$CONFIG_FILE"; then
    echo "⚠ Database already exists in $CONFIG_FILE"
else
    echo "$DB_NAME" >> "$CONFIG_FILE"
    echo "✓ Added $DB_NAME to $CONFIG_FILE"
fi
echo ""

echo "==========================================="
echo "✓ Site creation complete!"
echo "==========================================="
echo "Database: $DB_NAME"
echo "Company: $SITE_NAME"
echo "POS: $SITE_NAME"
echo "==========================================="
