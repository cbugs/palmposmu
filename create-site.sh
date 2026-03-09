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

# Step 5: Regenerate database UUID to prevent cache conflicts
echo "Step 5: Regenerating database UUID..."
NEW_UUID=$(cat /proc/sys/kernel/random/uuid 2>/dev/null || uuidgen)
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "UPDATE ir_config_parameter SET value = '$NEW_UUID' WHERE key = 'database.uuid';"

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Could not update database UUID"
else
    echo "✓ Database UUID regenerated"
fi
echo ""

# Step 6: Clear and regenerate assets
echo "Step 6: Clearing cached assets and sessions..."
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "DELETE FROM ir_attachment WHERE name LIKE 'web.assets%' OR name LIKE '%web_icon_data%' OR res_model = 'ir.ui.view';"
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "DELETE FROM ir_sessions;"
PGPASSWORD="$POSTGRES_PASSWORD" psql -d "$DB_NAME" -U "$POSTGRES_USER" -h localhost -c "UPDATE ir_ui_view SET write_date = NOW();"

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Could not clear cached assets"
else
    echo "✓ Cached assets, sessions, and views cleared"
fi
echo ""

# Step 7: Regenerate assets by updating base module
echo "Step 7: Regenerating assets and updating all modules..."
docker exec palmpos_app odoo -d "$DB_NAME" -u base,point_of_sale,muk_web_appsbar,muk_web_chatter,muk_web_colors,muk_web_dialog,muk_web_group,muk_web_refresh,muk_web_theme,palmpos_contact,palmpos_theme,palmpos_title,pos_auto_redirect,pos_screensaver,pos_receipt_customize,palmpos_profit_report,web_replace_url --stop-after-init

if [ $? -ne 0 ]; then
    echo "⚠ Warning: Module update may have failed"
else
    echo "✓ All modules updated and assets regenerated successfully"
fi
echo ""

# Step 8: Add to databases.conf
echo "Step 8: Adding to $CONFIG_FILE..."
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
