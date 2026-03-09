#!/bin/bash

# Script to update a module across multiple databases
# Usage: ./update-module.sh module_name

if [ -z "$1" ]; then
    echo "Error: Module name is required"
    echo "Usage: ./update-module.sh module_name"
    exit 1
fi

MODULE=$1

# Load databases from config file
CONFIG_FILE="databases.conf"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: $CONFIG_FILE not found"
    echo "Please create $CONFIG_FILE with one database name per line"
    echo "See databases.conf.example for reference"
    exit 1
fi

# Read databases from config file, ignoring comments and empty lines
DATABASES=()
while IFS= read -r line || [ -n "$line" ]; do
    # Skip comments and empty lines
    [[ "$line" =~ ^[[:space:]]*# ]] && continue
    [[ -z "${line// }" ]] && continue
    # Trim whitespace and add to array
    db=$(echo "$line" | xargs)
    DATABASES+=("$db")
done < "$CONFIG_FILE"

# Check if we have any databases
if [ ${#DATABASES[@]} -eq 0 ]; then
    echo "Error: No databases found in $CONFIG_FILE"
    exit 1
fi

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
