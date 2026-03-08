# POS Kitchen Display System (KDS) Setup Guide

## Overview
The KDS system shows orders from the POS on a kitchen screen. Orders only appear when properly configured.

## Configuration Steps

### Step 1: Create POS Categories
POS Categories are used to route specific products to specific kitchen screens.

1. Go to **Point of Sale → Configuration → POS Product Categories**
2. Click **New** and create categories like:
   - Hot Food
   - Drinks
   - Desserts  
   - Cold Food
3. Save each category

### Step 2: Configure Kitchen Screen
Link the kitchen screen to your POS and assign categories.

1. Go to **Point of Sale → Kitchen → Kitchen Screen**
2. You'll see a record **KITCHEN0001** - open it
3. Set **Allowed POS**: Select your POS configuration (e.g., "Shop -Main")
4. Set **Allowed POS Category**: Select the categories you want to show on this screen
   - Example: Select "Hot Food" and "Drinks"
5. Click **Save**

**Important**: Each kitchen screen can only be linked to ONE POS configuration.

### Step 3: Assign Categories to Products
Products must have matching categories to appear on the kitchen screen.

1. Go to **Inventory → Products → Products**
2. Open a product (e.g., "Pizza")
3. Scroll down to the **Sales** tab
4. Find **Kitchen Display System** section
5. In **Kitchen Categories**, select categories like "Hot Food"
6. Click **Save**
7. Repeat for all products that should appear in the kitchen

**Tip**: Use bulk actions to assign categories to multiple products at once.

### Step 4: Test the System

1. **Open KDS Screen** (on one device/browser):
   - Go to **Point of Sale → Kitchen → Kitchen Screen**
   - Click on **KITCHEN0001**
   - Click the **Kitchen Screen** smart button (top right)
   - This opens the fullscreen KDS view

2. **Open POS** (on another device/browser):
   - Go to **Point of Sale → New Session**
   - Click **Open Session**
   - Select a table
   - Add a product that has a kitchen category assigned
   - Click **Order** button

3. **Check KDS Screen**:
   - The order should immediately appear on the kitchen screen
   - You'll see: Table name, Order items, Quantity, Time

## Kitchen Screen Actions

On the KDS screen, kitchen staff can:

- **Accept** - Moves order from "Cooking" to "Ready" status  
- **Cancel** - Cancels the order
- **Done** - Marks order as completed (removes from screen)

## Order Flow

```
POS Order Created → KDS shows "Cooking" → Accept → "Ready" → Done → "Completed"
```

## Troubleshooting

### Orders Not Appearing?

**Check 1**: Does the kitchen screen have a POS config assigned?
- Go to Kitchen Screen configuration
- Verify **Allowed POS** field is filled

**Check 2**: Does the kitchen screen have categories assigned?
- Go to Kitchen Screen configuration  
- Verify **Allowed POS Category** field has at least one category

**Check 3**: Do products have matching categories?
- Open a product you're trying to order
- Check **Sales** tab → **Kitchen Display System** section
- Verify **Kitchen Categories** matches what's on the kitchen screen

**Check 4**: Are you using the correct POS?
- The kitchen screen only shows orders from its linked POS config
- If you create orders from a different POS, they won't appear

### Orders Appear But Then Disappear?

- Check the order status - completed orders are hidden by default
- The KDS only shows orders with status: draft (cooking), waiting (ready), ready (completed recently)

## Multiple Kitchen Screens

You can create multiple kitchen screens for different purposes:

**Example Setup**:
- **Kitchen Screen 1**: Linked to "Main POS", Categories: Hot Food, Desserts
- **Kitchen Screen 2**: Linked to "Main POS", Categories: Drinks, Cold Food  
- **Kitchen Screen 3**: Linked to "Takeaway POS", Categories: All

This allows different kitchen stations to see only relevant orders.

## Advanced: Preparation Time

You can set preparation time for products:
1. Open product 
2. Find **Preparation Time (MM:SS)** field
3. Enter time like 20.5 (20 minutes 30 seconds)
4. This shows estimated completion time on KDS

## Quick Reference

| What You Need | Where to Configure |
|---------------|-------------------|
| Create categories | Point of Sale → Configuration → POS Product Categories |
| Link screen to POS | Point of Sale → Kitchen → Kitchen Screen |
| Assign categories to products | Inventory → Products → Sales tab |
| View KDS | Point of Sale → Kitchen → Kitchen Screen → Kitchen Screen button |
| Create orders | Point of Sale → New Session |

---

**Note**: Orders placed BEFORE configuration won't appear. Only new orders after proper setup will show on the KDS.
