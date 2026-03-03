#!/bin/bash
# PostgreSQL Database Backup Script
# This script creates a pg_dump backup with timestamp

# Default parameters
DB_NAME="${1:-palmpos}"
DB_USER="${2:-palmpos}"
DB_PASSWORD="${3:-palmpos}"
DB_HOST="${4:-localhost}"
DB_PORT="${5:-5432}"

# Create backup directory if it doesn't exist
BACKUP_DIR="$(dirname "$0")/backup"
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
fi

# Generate timestamp for backup filename
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/palmpos_backup_$TIMESTAMP.dump"

echo "Starting database backup..."
echo "Database: $DB_NAME"
echo "Host: $DB_HOST:$DB_PORT"
echo "User: $DB_USER"
echo "Destination: $BACKUP_FILE"

# Set password for pg_dump
export PGPASSWORD="$DB_PASSWORD"

# Create backup using pg_dump (custom format - compressed and restorable)
pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -Fc -f "$BACKUP_FILE"

RESULT=$?
unset PGPASSWORD

if [ $RESULT -eq 0 ] && [ -f "$BACKUP_FILE" ]; then
    FILE_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo -e "\033[0;32mBackup completed successfully!\033[0m"
    echo "File: $BACKUP_FILE"
    echo "Size: $FILE_SIZE"
    echo ""
    echo "To restore this backup, run:"
    echo "  pg_restore -h $DB_HOST -p $DB_PORT -U $DB_USER -d <new_db_name> -c $BACKUP_FILE"
    
    # List recent backups
    echo ""
    echo "Recent backups:"
    ls -lht "$BACKUP_DIR"/*.dump 2>/dev/null | head -5 | while read -r line; do
        echo "  $line"
    done
else
    echo -e "\033[0;31mBackup failed!\033[0m"
    echo "Make sure PostgreSQL is running and credentials are correct."
    rm -f "$BACKUP_FILE" 2>/dev/null
    exit 1
fi
