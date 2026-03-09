#!/bin/bash

# Script to create a new site from template
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

echo "==========================================="
echo "Creating new site"
echo "==========================================="
echo "Site Name: $SITE_NAME"
echo "Slug: $SITE_SLUG"
echo "Database: $DB_NAME"
echo "Template: $TEMPLATE_DB"
echo "==========================================="
echo ""

# Step 1: Create database from template
echo "Step 1: Creating database from template..."
createdb "$DB_NAME" -T "$TEMPLATE_DB" -O palmpos

if [ $? -ne 0 ]; then
    echo "✗ Failed to create database"
    exit 1
fi
echo "✓ Database created successfully"
echo ""

# Step 2: Update company name
echo "Step 2: Updating company name to '$SITE_NAME'..."
psql -d "$DB_NAME" -c "UPDATE res_company SET name = '$SITE_NAME' WHERE id = 1;"

if [ $? -ne 0 ]; then
    echo "✗ Failed to update company name"
    exit 1
fi
echo "✓ Company name updated"
echo ""

# Step 3: Update Point of Sale name
echo "Step 3: Updating Point of Sale name to '$SITE_NAME'..."
psql -d "$DB_NAME" -c "UPDATE pos_config SET name = '$SITE_NAME' WHERE id = 1;"

if [ $? -ne 0 ]; then
    echo "✗ Failed to update POS name"
    exit 1
fi
echo "✓ Point of Sale name updated"
echo ""

# Step 4: Add to databases.conf
echo "Step 4: Adding to $CONFIG_FILE..."
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
