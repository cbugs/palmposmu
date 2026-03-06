#!/bin/bash

# Script to update a module across multiple databases
# Usage: ./update-module.sh module_name

if [ -z "$1" ]; then
    echo "Error: Module name is required"
    echo "Usage: ./update-module.sh module_name"
    exit 1
fi

MODULE=$1

# List of databases to update
DATABASES=(
    "palmpos_demo"
    "palmpos_bigpapa-rod",
    "palmpos_chumroo-market",
    "palmpos_cyberplast",
    "palmpos_hungry-buddha",
    "palmpos_mashwiyy",
    # Add more databases here as needed
)

echo "==========================================="
echo "Updating module: $MODULE"
echo "Databases: ${DATABASES[@]}"
echo "==========================================="

# Loop through all databases
for DB in "${DATABASES[@]}"; do
    echo ""
    echo "-------------------------------------------"
    echo "Updating $MODULE in database: $DB"
    echo "-------------------------------------------"
    docker exec -it palmpos_app odoo -d "$DB" -u "$MODULE" --stop-after-init
    
    if [ $? -eq 0 ]; then
        echo "✓ Successfully updated $MODULE in $DB"
    else
        echo "✗ Failed to update $MODULE in $DB"
    fi
done

echo ""
echo "==========================================="
echo "Update complete for all databases"
echo "==========================================="
