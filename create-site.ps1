# Script to create a new site from template
# Usage: .\create-site.ps1 "Site Name" "site-slug"
# Example: .\create-site.ps1 "Hungry Food" "hungry-food"

param(
    [Parameter(Mandatory=$true)]
    [string]$SiteName,
    
    [Parameter(Mandatory=$true)]
    [string]$SiteSlug
)

$DB_NAME = "palmpos_$SiteSlug"
$TEMPLATE_DB = "palmpos_template1"
$CONFIG_FILE = "databases.conf"
$ENV_FILE = ".env"

# Load database credentials from .env file
if (-not (Test-Path $ENV_FILE)) {
    Write-Host "Error: $ENV_FILE not found" -ForegroundColor Red
    exit 1
}

# Read specific values from .env file
$envContent = Get-Content $ENV_FILE
$POSTGRES_USER = ($envContent | Select-String "^POSTGRES_USER=").ToString().Split('=')[1]
$POSTGRES_PASSWORD = ($envContent | Select-String "^POSTGRES_PASSWORD=").ToString().Split('=')[1]

if ([string]::IsNullOrEmpty($POSTGRES_USER)) {
    Write-Host "Error: POSTGRES_USER not found in $ENV_FILE" -ForegroundColor Red
    exit 1
}

Write-Host "==========================================="
Write-Host "Creating new site"
Write-Host "==========================================="
Write-Host "Site Name: $SiteName"
Write-Host "Slug: $SiteSlug"
Write-Host "Database: $DB_NAME"
Write-Host "Template: $TEMPLATE_DB"
Write-Host "==========================================="
Write-Host ""

# Set PGPASSWORD environment variable for this session
$env:PGPASSWORD = $POSTGRES_PASSWORD

# Step 1: Terminate connections to template database
Write-Host "Step 1: Disconnecting users from template database..."
$result = psql -U $POSTGRES_USER -h localhost -d postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '$TEMPLATE_DB' AND pid <> pg_backend_pid();" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Could not terminate all connections" -ForegroundColor Yellow
} else {
    Write-Host "OK Template database ready" -ForegroundColor Green
}
Write-Host ""

# Step 2: Create database from template
Write-Host "Step 2: Creating database from template..."
$result = createdb $DB_NAME -T $TEMPLATE_DB -O $POSTGRES_USER -U $POSTGRES_USER -h localhost 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "X Failed to create database" -ForegroundColor Red
    exit 1
}
Write-Host "OK Database created successfully" -ForegroundColor Green
Write-Host ""

# Step 2.5: Copy filestore from template to new database
Write-Host "Step 2.5: Copying filestore from template..."
docker exec -u root palmpos_app rm -rf "/var/lib/odoo/.local/share/Odoo/filestore/$DB_NAME" 2>&1 | Out-Null
docker exec -u root palmpos_app cp -r "/var/lib/odoo/.local/share/Odoo/filestore/$TEMPLATE_DB" "/var/lib/odoo/.local/share/Odoo/filestore/$DB_NAME" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Could not copy filestore" -ForegroundColor Yellow
} else {
    docker exec -u root palmpos_app chown -R odoo:odoo "/var/lib/odoo/.local/share/Odoo/filestore/$DB_NAME" 2>&1 | Out-Null
    Write-Host "OK Filestore copied successfully" -ForegroundColor Green
}
Write-Host ""

# Step 3: Update company name
Write-Host "Step 3: Updating company name to '$SiteName'..."
$result = psql -d $DB_NAME -U $POSTGRES_USER -h localhost -c "UPDATE res_company SET name = '$SiteName' WHERE id = 1;" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "X Failed to update company name" -ForegroundColor Red
    exit 1
}
Write-Host "OK Company name updated" -ForegroundColor Green
Write-Host ""

# Step 4: Update Point of Sale name
Write-Host "Step 4: Updating Point of Sale name to '$SiteName'..."
$result = psql -d $DB_NAME -U $POSTGRES_USER -h localhost -c "UPDATE pos_config SET name = '$SiteName' WHERE id = 1;" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "X Failed to update POS name" -ForegroundColor Red
    exit 1
}
Write-Host "OK Point of Sale name updated" -ForegroundColor Green
Write-Host ""

# Step 4.5: Update owner user name
Write-Host "Step 4.5: Updating owner user name to '$SiteName'..."
$result = psql -d $DB_NAME -U $POSTGRES_USER -h localhost -c "UPDATE res_partner SET name = '$SiteName' WHERE id = (SELECT partner_id FROM res_users WHERE login = 'owner');" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Could not update owner user name" -ForegroundColor Yellow
} else {
    Write-Host "OK Owner user name updated" -ForegroundColor Green
}
Write-Host ""

# Step 4.6: Regenerate asset bundles
Write-Host "Step 4.6: Regenerating asset bundles..."
$result = docker exec palmpos_app odoo shell -d $DB_NAME --db_host=host.docker.internal --db_user=$POSTGRES_USER --db_password=$POSTGRES_PASSWORD -c "self.env['ir.attachment'].regenerate_assets_bundles(); self.env.cr.commit(); exit()" 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Could not regenerate assets" -ForegroundColor Yellow
} else {
    Write-Host "OK Asset bundles regenerated" -ForegroundColor Green
}
Write-Host ""

# Step 5: Add to databases.conf
Write-Host "Step 5: Adding to $CONFIG_FILE..."
if (-not (Test-Path $CONFIG_FILE)) {
    Write-Host "Warning: $CONFIG_FILE not found, creating it" -ForegroundColor Yellow
    @"
# List of databases for update-module.sh
# One database name per line

"@ | Out-File -FilePath $CONFIG_FILE -Encoding utf8
}

# Check if database already exists in config
$existingDbs = Get-Content $CONFIG_FILE | Where-Object { $_ -eq $DB_NAME }
if ($existingDbs) {
    Write-Host "Warning: Database already exists in $CONFIG_FILE" -ForegroundColor Yellow
} else {
    Add-Content -Path $CONFIG_FILE -Value $DB_NAME
    Write-Host "OK Added $DB_NAME to $CONFIG_FILE" -ForegroundColor Green
}
Write-Host ""

Write-Host "==========================================="
Write-Host "OK Site creation complete!" -ForegroundColor Green
Write-Host "==========================================="
Write-Host "Database: $DB_NAME"
Write-Host "Company: $SiteName"
Write-Host "POS: $SiteName"
Write-Host "==========================================="
