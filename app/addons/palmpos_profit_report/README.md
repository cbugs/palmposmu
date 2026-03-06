# PalmPOS Profit & Loss Report

A comprehensive profit and loss reporting module for Odoo 19.0 Point of Sale.

## Features

### 📊 Multiple Report Types
- **Profit by Product** - See which products generate the most profit
- **Profit by Customer** - Analyze customer profitability  
- **Profit by Date** - Track profit trends over time

### 💰 Detailed Metrics
Each report shows:
- **Quantity Sold** - Total units sold
- **Sales Amount** - Total revenue including tax
- **Cost Amount** - Cost of goods sold
- **Tax Amount** - Total tax collected
- **Discount Amount** - Total discounts given
- **Profit Amount** - Net profit (Sales - Cost)
- **Profit Margin %** - Profitability percentage

### 📥 Export Options
- **PDF Export** - Professional print-ready reports
- **Excel Export** - Detailed spreadsheets for further analysis

### 🔍 Flexible Filtering
Filter reports by:
- Date range (from/to)
- POS sessions
- Specific products
- Product categories
- Customers

## Installation

1. The addon is already included in the Makefile
2. Restart Odoo: `make restart`
3. Update the addon list in Odoo
4. Install "PalmPOS Profit & Loss Report"

## Usage

### Generate a Report

1. Go to **Point of Sale → POS Profits → Generate Report**
2. Select report type (Product, Customer, or Date)
3. Choose date range
4. (Optional) Filter by sessions, products, categories, or customers
5. Click **Generate Report**

### View Report

The report displays:
- A detailed table with all metrics
- Summary totals at the bottom
- Profit margins highlighted (green for profit, red for loss)

### Export Report

From the report view:
- Click **Print PDF** for a formatted PDF document
- Click **Export Excel** for an Excel spreadsheet with formulas

## Example Report

```
Product Report (March 1-5, 2026)

Product               Qty    Sales     Cost      Tax    Discount  Profit   Margin %
─────────────────────────────────────────────────────────────────────────────────
Coffee                120    $600.00   $250.00   $30    $10.00    $350.00  58.33%
Sandwich              80     $400.00   $180.00   $20    $5.00     $220.00  55.00%
Salad                 45     $225.00   $110.00   $11    $0.00     $115.00  51.11%
─────────────────────────────────────────────────────────────────────────────────
TOTAL                 245    $1,225.00 $540.00   $61    $15.00    $685.00  55.92%
```

## Technical Details

### Models

- `pos.profit.report` - Main report model
- `pos.profit.report.line` - Individual report lines
- `profit.report.wizard` - Report generation wizard

### Dependencies

- `point_of_sale` - Odoo POS module
- `stock` - For product cost calculation

### Cost Calculation

Product costs are taken from the **Cost** field (standard_price) on the product form. Make sure your product costs are up to date for accurate profit calculations.

## Menu Location

Access reports from:
**Point of Sale → POS Profits**

Submenu items:
- **Profit Reports** - View all generated reports
- **Generate Report** - Create a new report

## Tips

1. **Regular Updates** - Generate reports regularly to track profit trends
2. **Product Costs** - Keep product costs updated for accurate calculations
3. **Date Ranges** - Use custom date ranges to analyze specific periods
4. **Category Analysis** - Filter by categories to analyze product lines
5. **Customer Insights** - Use customer reports to identify top buyers

## Support

For issues or questions, contact your PalmPOS administrator.

## License

LGPL-3

## Version

19.0.1.0.0
