<template>
  <div class="user-guide">
    <!-- Header -->
    <div class="guide-header">
      <div class="container">
        <div class="header-content">
          <img src="/palmpos.png" alt="PalmPOS" class="header-logo">
          <div class="header-text">
            <h1>PalmPOS User Guide</h1>
            <p>Complete documentation for Point of Sale and Inventory Management</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Navigation -->
    <nav class="guide-nav no-print">
      <div class="container">
        <a href="#getting-started" :class="{ active: activeSection === 'getting-started' }" @click.prevent="scrollToSection('getting-started')">Getting Started</a>
        <a href="#pos" :class="{ active: activeSection === 'pos' }" @click.prevent="scrollToSection('pos')">Point of Sale</a>
        <a href="#inventory" :class="{ active: activeSection === 'inventory' }" @click.prevent="scrollToSection('inventory')">Inventory</a>
        <a href="#reports" :class="{ active: activeSection === 'reports' }" @click.prevent="scrollToSection('reports')">Reports</a>
        <a href="#troubleshooting" :class="{ active: activeSection === 'troubleshooting' }" @click.prevent="scrollToSection('troubleshooting')">Troubleshooting</a>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container main-content">

      <!-- Getting Started -->
      <section id="getting-started" class="section-card">
        <div class="section-header">
          <i class="pi pi-book section-icon"></i>
          <div>
            <h2>Getting Started</h2>
            <p class="section-subtitle">Your first steps with PalmPOS</p>
          </div>
        </div>

        <div class="content-box">
          <h3>Logging In</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Open your browser and navigate to your PalmPOS URL</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Enter your email address or username</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Enter your password</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Click <span class="badge-custom">Log in</span></span>
            </li>
          </ol>
        </div>

        <div class="content-box highlight-box">
          <h3>Installing as an App</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Open the POS register interface</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Click the hamburger menu <span class="badge-custom">☰</span> (three horizontal lines)</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Select <span class="badge-custom">Install App</span></span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>PalmPOS will now be installed as a standalone application on your device</span>
            </li>
          </ol>
          <p class="info-note"><i class="pi pi-lightbulb"></i> <strong>Note:</strong> This allows PalmPOS to work offline and provides a better experience.</p>
        </div>

        <div class="content-box">
          <h3>Dashboard Overview</h3>
          <p>After logging in, you'll see the main dashboard with access to:</p>
          <div class="feature-grid">
            <div class="feature-item">
              <i class="pi pi-check feature-check"></i>
              <div>
                <strong>Point of Sale</strong>
                <p>Process sales transactions</p>
              </div>
            </div>
            <div class="feature-item">
              <i class="pi pi-check feature-check"></i>
              <div>
                <strong>Inventory</strong>
                <p>Manage products and stock</p>
              </div>
            </div>
            <div class="feature-item">
              <i class="pi pi-check feature-check"></i>
              <div>
                <strong>Reports</strong>
                <p>View sales analytics</p>
              </div>
            </div>
          </div>
        </div>

        <div class="content-box">
          <h3>Changing Your Password</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Click on your profile icon in the top right corner</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select <span class="badge-custom">My Profile</span> or <span class="badge-custom">Preferences</span></span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Go to the <span class="badge-custom">Account Security</span> section</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Click <span class="badge-custom">Change Password</span></span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Enter your current password</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Enter your new password and confirm it</span>
            </li>
            <li>
              <span class="step-number">7</span>
              <span>Click <span class="badge-custom">Save</span> to update your password</span>
            </li>
          </ol>
          <p class="info-note"><i class="pi pi-lightbulb"></i> <strong>Security Tip:</strong> Use a strong password with a mix of letters, numbers, and symbols.</p>
        </div>
      </section>

      <!-- Point of Sale -->
      <section id="pos" class="section-card">
        <div class="section-header">
          <i class="pi pi-shopping-cart section-icon"></i>
          <div>
            <h2>Point of Sale</h2>
            <p class="section-subtitle">Processing sales and transactions</p>
          </div>
        </div>

        <div class="content-box">
          <h3>Opening a POS Session</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Click <span class="badge-custom">Point of Sale</span> from the main menu</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select your POS terminal/register</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Click <span class="badge-custom">Open Session</span></span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Enter your cash float amount (optional)</span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Click <span class="badge-custom">Open Session</span> to start</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Making a Sale</h3>
          
          <h4 class="sub-heading">Step 1: Add Products</h4>
          <ul class="bullet-list">
            <li>Click on product tiles to add them to the cart</li>
            <li>Use the search bar to find specific products quickly</li>
            <li>Scan barcodes using a barcode scanner</li>
            <li>Adjust quantities by clicking on the line item</li>
          </ul>

          <h4 class="sub-heading">Step 2: Add Customer (Optional)</h4>
          <ul class="bullet-list">
            <li>Click the <span class="badge-custom">Customer</span> button</li>
            <li>Search for existing customer or create a new one</li>
            <li>Select the customer to add to the transaction</li>
          </ul>

          <h4 class="sub-heading">Step 3: Complete Payment</h4>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Click <span class="badge-custom">Payment</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select payment method (Cash, Card, Bank Transfer, etc.)</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Enter the amount received</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Click <span class="badge-custom">Validate</span></span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Receipt will print automatically (if printer configured)</span>
            </li>
          </ol>
        </div>

        <div class="content-box highlight-box">
          <h3>WhatsApp Receipt Sharing</h3>
          <p>After completing a sale, you can share the receipt via WhatsApp:</p>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Complete the payment</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Click the WhatsApp icon on the receipt screen</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Enter the customer's phone number (with country code)</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Receipt image will be sent via WhatsApp</span>
            </li>
          </ol>
          <p class="info-note"><i class="pi pi-lightbulb"></i> <strong>Tip:</strong> This is useful for customers who don't want a printed receipt or need a digital copy.</p>
        </div>

        <div class="content-box">
          <h3>Processing Refunds</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Click <span class="badge-custom">Orders</span> button in POS</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Find and select the order to refund</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Click <span class="badge-custom">Refund</span></span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Select items to refund (or all)</span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Confirm the refund</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Process the refund payment back to customer</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Closing a POS Session</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Click the menu <span class="badge-custom">☰</span> (three horizontal lines)</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select <span class="badge-custom">Close Session</span></span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Count and enter the actual cash in drawer</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Review the session summary</span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Click <span class="badge-custom">Close Session</span> to finalize</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Print Z-Report (end of day report)</span>
            </li>
          </ol>
        </div>
      </section>

      <!-- Inventory Management -->
      <section id="inventory" class="section-card">
        <div class="section-header">
          <i class="pi pi-box section-icon"></i>
          <div>
            <h2>Inventory Management</h2>
            <p class="section-subtitle">Products, stock, and suppliers</p>
          </div>
        </div>

        <div class="content-box">
          <h3>Adding Products</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Inventory</span> → <span class="badge-custom">Products</span> → <span class="badge-custom">Products</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Click <span class="badge-custom">New</span></span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Enter product name</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Set the sales price and cost</span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Add barcode (optional but recommended)</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Select product category</span>
            </li>
            <li>
              <span class="step-number">7</span>
              <span>Upload product image (optional)</span>
            </li>
            <li>
              <span class="step-number">8</span>
              <span>Check <span class="badge-custom">Available in POS</span></span>
            </li>
            <li>
              <span class="step-number">9</span>
              <span>Click <span class="badge-custom">Save</span></span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Managing Stock Levels</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Inventory</span> → <span class="badge-custom">Operations</span> → <span class="badge-custom">Stock</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>View current stock levels for all products</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Use filters to find specific products</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Click on a product to see detailed stock movements</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Stock Adjustments</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Inventory</span> → <span class="badge-custom">Operations</span> → <span class="badge-custom">Adjustments</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Click <span class="badge-custom">New</span></span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Select the location</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Click <span class="badge-custom">Add a product</span></span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Select product and enter the correct quantity</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Add reason for adjustment (optional)</span>
            </li>
            <li>
              <span class="step-number">7</span>
              <span>Click <span class="badge-custom">Apply</span> to update stock</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Receiving Stock (Purchase Orders)</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Inventory</span> → <span class="badge-custom">Operations</span> → <span class="badge-custom">Receipts</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Click <span class="badge-custom">New</span></span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Select the vendor/supplier</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Add products and quantities</span>
            </li>
            <li>
              <span class="step-number">5</span>
              <span>Click <span class="badge-custom">Validate</span> when stock arrives</span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>Stock will be automatically added to inventory</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Low Stock Alerts</h3>
          <p>Set minimum stock levels to get automatic alerts:</p>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Open any product</span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Go to <span class="badge-custom">Inventory</span> tab</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Set <span class="badge-custom">Minimum Quantity</span></span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>System will alert when stock falls below this level</span>
            </li>
          </ol>
        </div>
      </section>

      <!-- Reports -->
      <section id="reports" class="section-card">
        <div class="section-header">
          <i class="pi pi-chart-bar section-icon"></i>
          <div>
            <h2>Reports & Analytics</h2>
            <p class="section-subtitle">Track performance and insights</p>
          </div>
        </div>

        <div class="content-box">
          <h3>Sales Details Report (X/Z Report)</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Point of Sale</span> → <span class="badge-custom">Reporting</span> → <span class="badge-custom">Sessions</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select the session you want to view</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Click <span class="badge-custom">Print</span> to generate the report</span>
            </li>
          </ol>
          
          <div class="info-box">
            <p><strong>What's the difference between X and Z reports?</strong></p>
            <ul class="bullet-list">
              <li><strong>X-Report (Mid-day):</strong> Can be printed anytime during an open session without closing it. Good for checking sales progress.</li>
              <li><strong>Z-Report (End of day):</strong> Printed when closing a session. This is your final daily sales report.</li>
            </ul>
          </div>
        </div>

        <div class="content-box">
          <h3>Profit Report</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Point of Sale</span> → <span class="badge-custom">Reporting</span> → <span class="badge-custom">Profit Report</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>Select date range</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Choose POS terminals to include</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Select report type:</span>
            </li>
          </ol>
          
          <div class="feature-grid">
            <div class="feature-item">
              <i class="pi pi-box feature-icon"></i>
              <div>
                <strong>By Product</strong>
                <p>See profit for each product</p>
              </div>
            </div>
            <div class="feature-item">
              <i class="pi pi-user feature-icon"></i>
              <div>
                <strong>By Customer</strong>
                <p>See profit per customer</p>
              </div>
            </div>
            <div class="feature-item">
              <i class="pi pi-calendar feature-icon"></i>
              <div>
                <strong>By Date</strong>
                <p>See daily profit trends</p>
              </div>
            </div>
          </div>

          <ol class="step-list" start="5">
            <li>
              <span class="step-number">5</span>
              <span>Click <span class="badge-custom">Generate Report</span></span>
            </li>
            <li>
              <span class="step-number">6</span>
              <span>View on screen or download PDF/Excel</span>
            </li>
          </ol>
        </div>

        <div class="content-box">
          <h3>Inventory Reports</h3>
          <ol class="step-list">
            <li>
              <span class="step-number">1</span>
              <span>Go to <span class="badge-custom">Inventory</span> → <span class="badge-custom">Reporting</span> → <span class="badge-custom">Stock</span></span>
            </li>
            <li>
              <span class="step-number">2</span>
              <span>View current stock levels</span>
            </li>
            <li>
              <span class="step-number">3</span>
              <span>Filter by location, category, or product</span>
            </li>
            <li>
              <span class="step-number">4</span>
              <span>Export to Excel using the <span class="badge-custom">📥</span> icon</span>
            </li>
          </ol>
        </div>
      </section>

      <!-- Troubleshooting -->
      <section id="troubleshooting" class="section-card">
        <div class="section-header">
          <i class="pi pi-wrench section-icon"></i>
          <div>
            <h2>Troubleshooting</h2>
            <p class="section-subtitle">Common issues and solutions</p>
          </div>
        </div>

        <div class="problem-grid">
          <div class="problem-card">
            <h3><i class="pi pi-times-circle"></i> POS Won't Open</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>Check if a session is already open</li>
              <li>Close any existing session first</li>
              <li>Refresh the browser and try again</li>
              <li>Contact support if issue persists</li>
            </ul>
          </div>

          <div class="problem-card">
            <h3><i class="pi pi-print"></i> Printer Not Working</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>Check printer is powered on and connected</li>
              <li>Verify printer has paper</li>
              <li>Check USB/network cable connection</li>
              <li>Restart printer and try again</li>
              <li>Check printer settings in POS configuration</li>
            </ul>
          </div>

          <div class="problem-card">
            <h3><i class="pi pi-chart-bar"></i> Products Not Showing</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>Check product has "Available in POS" enabled</li>
              <li>Verify product has a valid price</li>
              <li>Refresh POS session</li>
              <li>Check if product is in correct category</li>
            </ul>
          </div>

          <div class="problem-card">
            <h3><i class="pi pi-money-bill"></i> Wrong Cash Count</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>Recount physical cash carefully</li>
              <li>Check for missed transactions</li>
              <li>Verify all payments are recorded</li>
              <li>Document any discrepancies</li>
              <li>Adjust if needed with supervisor approval</li>
            </ul>
          </div>

          <div class="problem-card">
            <h3><i class="pi pi-globe"></i> Working Offline</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>POS continues to work without internet</li>
              <li>Orders are saved locally</li>
              <li>Once internet returns, data syncs automatically</li>
              <li>Avoid closing browser during offline mode</li>
            </ul>
          </div>

          <div class="problem-card">
            <h3><i class="pi pi-refresh"></i> Need to Refund Old Order</h3>
            <p><strong>Solution:</strong></p>
            <ul class="bullet-list">
              <li>Go to POS → Reporting → Orders</li>
              <li>Search for the order by receipt number or customer</li>
              <li>Open the order and click Refund</li>
              <li>Complete refund process</li>
            </ul>
          </div>
        </div>

        <div class="content-box highlight-box">
          <h3><i class="pi pi-phone"></i> Need More Help?</h3>
          <p>If you encounter any issues not covered here:</p>
          <ul class="bullet-list">
            <li><strong>Email:</strong> support@palmposmu.com</li>
          </ul>
        </div>
      </section>

      <!-- Quick Reference -->
      <section class="section-card quick-ref">
        <div class="section-header centered">
          <h2><i class="pi pi-bolt"></i> Quick Reference</h2>
          <p class="section-subtitle">Common actions at a glance</p>
        </div>
        
        <div class="quick-ref-grid">
          <div class="quick-ref-col">
            <h3>Common POS Actions</h3>
            <ul class="quick-list">
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Open Session:</strong> POS → Select POS → Open Session</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Make Sale:</strong> Add products → Payment → Validate</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Add Customer:</strong> Click "Customer" → Select/Create</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Add Discount:</strong> Click "% Disc" button</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Process Refund:</strong> Orders → Select → Refund</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Close Session:</strong> Menu (☰) → Close Session</li>
            </ul>
          </div>
          
          <div class="quick-ref-col">
            <h3>Report Shortcuts</h3>
            <ul class="quick-list">
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Sales Details:</strong> POS → Reporting → Sessions</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Profit Report:</strong> POS → Reporting → Profit Report</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Inventory:</strong> Inventory → Reporting → Stock</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Export Excel:</strong> Click Excel icon in reports</li>
              <li><i class="pi pi-arrow-right arrow"></i> <strong>Print Report:</strong> Click Print button</li>
            </ul>
          </div>
        </div>

        <div class="tip-box">
          <p><i class="pi pi-lightbulb"></i> <strong>Pro Tip:</strong> Bookmark this page in your browser for quick access to the user guide!</p>
        </div>
      </section>

    </div>

    <!-- Footer -->
    <footer class="guide-footer">
      <div class="container">
        <h3>PalmPOS</h3>
        <p class="footer-subtitle">User Guide & Documentation</p>
        <p class="footer-desc">Complete documentation for Point of Sale and Inventory Management</p>
        <p class="footer-version">Version 1.0 - March 2026</p>
      </div>
    </footer>

    <!-- Print Button -->
    <button class="print-btn no-print" @click="printPage">
      <i class="pi pi-file-pdf"></i>
      <span>Print / Save PDF</span>
    </button>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';

const activeSection = ref('getting-started');

const printPage = () => {
  window.print();
};

const loadCSS = (href) => {
  return new Promise((resolve, reject) => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    link.onload = resolve;
    link.onerror = reject;
    document.head.appendChild(link);
  });
};

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId);
  if (element) {
    const navHeight = document.querySelector('.guide-nav').offsetHeight;
    const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
    const offsetPosition = elementPosition - navHeight - 20; // 20px extra padding
    
    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    });
  }
};

const handleScroll = () => {
  const sections = ['getting-started', 'pos', 'inventory', 'reports', 'troubleshooting'];
  const navHeight = document.querySelector('.guide-nav')?.offsetHeight || 0;
  
  for (const sectionId of sections) {
    const element = document.getElementById(sectionId);
    if (element) {
      const rect = element.getBoundingClientRect();
      // Check if section is in view (accounting for nav height)
      if (rect.top <= navHeight + 100 && rect.bottom >= navHeight + 100) {
        activeSection.value = sectionId;
        break;
      }
    }
  }
};

onMounted(async () => {
  // Load PrimeIcons
  try {
    await loadCSS('https://unpkg.com/primeicons@7.0.0/primeicons.css');
  } catch (error) {
    console.error('Failed to load PrimeIcons:', error);
  }
  
  // Add scroll listener for scroll spy
  window.addEventListener('scroll', handleScroll);
  // Initial check
  handleScroll();
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  box-sizing: border-box;
}

.user-guide {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: white;
  min-height: 100vh;
  color: #111827;
  font-size: 14px;
  line-height: 1.5;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Header */
.guide-header {
  text-align: center;
  padding: 1.75rem 1.5rem 1.5rem;
  background: white;
  color: #111827;
}

.header-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.header-logo {
  width: 48px;
  height: 48px;
  margin: 0 auto 0.75rem;
  display: block;
}

.header-text h1 {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: #111827;
}

.header-text p {
  font-size: 1rem;
  color: #6b7280;
  margin: 0;
}

/* Navigation */
.guide-nav {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
}

.guide-nav .container {
  display: flex;
  gap: 24px;
  overflow-x: auto;
}

.guide-nav a {
  padding: 12px 0;
  color: #6b7280;
  text-decoration: none;
  font-weight: 500;
  font-size: 14px;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
}

.guide-nav a:hover {
  color: #10b981;
  border-bottom-color: #10b981;
}

.guide-nav a.active {
  color: #10b981;
  border-bottom-color: #10b981;
  font-weight: 600;
}

/* Main Content */
.main-content {
  padding: 48px 24px;
}

/* Sections */
.section-card {
  background: white;
  border-radius: 12px;
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
  scroll-margin-top: 80px; /* Offset for sticky nav */
}

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.section-header.centered {
  flex-direction: column;
  text-align: center;
  gap: 8px;
}

.section-header.centered h2 {
  justify-content: center;
}

.section-icon {
  font-size: 36px;
  color: #10b981;
  flex-shrink: 0;
}

.section-header h2 {
  font-size: 24px;
  font-weight: 700;
  color: #111827;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-header h2 i {
  color: #10b981;
}

.section-subtitle {
  color: #6b7280;
  font-size: 14px;
  margin: 4px 0 0 0;
}

/* Content Boxes */
.content-box {
  background: linear-gradient(to bottom right, #f9fafb, #f3f4f6);
  border-radius: 10px;
  padding: 24px;
  margin-bottom: 20px;
  border: 1px solid #e5e7eb;
}

.content-box:last-child {
  margin-bottom: 0;
}

.highlight-box {
  background: linear-gradient(to bottom right, #d1fae5, #a7f3d0);
  border: 2px solid #6ee7b7;
}

.content-box h3 {
  font-size: 17px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 14px 0;
  display: flex;
  align-items: center;
  gap: 6px;
}

.content-box h3 i {
  color: #10b981;
}

.sub-heading {
  font-size: 15px;
  font-weight: 600;
  color: #374151;
  margin: 16px 0 10px 0;
}

/* Lists */
.step-list {
  list-style: none;
  padding: 0;
  margin: 12px 0;
}

.step-list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 12px;
  line-height: 1.5;
}

.step-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  line-height: 24px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-weight: 600;
  font-size: 12px;
  flex-shrink: 0;
  text-align: center;
}

.bullet-list {
  list-style: none;
  padding: 0;
  margin: 12px 0;
}

.bullet-list li {
  padding-left: 20px;
  position: relative;
  margin-bottom: 6px;
  line-height: 1.5;
}

.bullet-list li:before {
  content: '•';
  position: absolute;
  left: 8px;
  color: #10b981;
  font-weight: 700;
}

/* Badges */
.badge-custom {
  display: inline-block;
  padding: 3px 10px;
  background: #10b981;
  color: white;
  border-radius: 5px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  line-height: 1.4;
  vertical-align: middle;
}

/* Feature Grid */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.feature-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.feature-check {
  color: #10b981;
  font-size: 18px;
  flex-shrink: 0;
}

.feature-icon {
  font-size: 24px;
  color: #10b981;
  flex-shrink: 0;
}

.feature-item strong {
  display: block;
  color: #111827;
  margin-bottom: 3px;
  font-size: 14px;
}

.feature-item p {
  color: #6b7280;
  font-size: 13px;
  margin: 0;
}

/* Info Box */
.info-box {
  background: white;
  border-left: 4px solid #10b981;
  padding: 12px;
  margin-top: 16px;
  border-radius: 4px;
}

.info-note {
  background: rgba(16, 185, 129, 0.1);
  border-left: 4px solid #10b981;
  padding: 12px;
  margin-top: 16px;
  border-radius: 4px;
  font-size: 13px;
}

.info-note i {
  color: #10b981;
  margin-right: 4px;
}

/* Problem Grid */
.problem-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.problem-card {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  padding: 20px;
}

.problem-card h3 {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 10px 0;
}

.problem-card h3 i {
  color: #10b981;
  margin-right: 8px;
}

.problem-card p {
  font-weight: 600;
  color: #374151;
  margin: 0 0 6px 0;
  font-size: 14px;
}

/* Quick Reference */
.quick-ref {
  background: white;
}

.quick-ref-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  gap: 24px;
  margin-bottom: 20px;
}

.quick-ref-col h3 {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 14px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid #6ee7b7;
}

.quick-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.quick-list li {
  padding: 8px 0;
  color: #4b5563;
  line-height: 1.5;
  display: flex;
  align-items: flex-start;
  gap: 6px;
}

.arrow {
  color: #10b981;
  font-size: 14px;
  flex-shrink: 0;
  margin-top: 2px;
}

.tip-box {
  background: linear-gradient(to bottom right, #d1fae5, #a7f3d0);
  border: 2px solid #6ee7b7;
  border-radius: 10px;
  padding: 18px;
  text-align: center;
}

.tip-box p {
  margin: 0;
  color: #4b5563;
}

.tip-box i {
  color: #10b981;
  margin-right: 4px;
}

/* Footer */
.guide-footer {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  padding: 32px 0;
  margin-top: 48px;
  text-align: center;
}

.guide-footer h3 {
  font-size: 22px;
  font-weight: 700;
  margin: 0 0 6px 0;
}

.footer-subtitle {
  color: rgba(255, 255, 255, 0.9);
  margin: 0 0 3px 0;
  font-size: 15px;
}

.footer-desc {
  color: rgba(255, 255, 255, 0.7);
  font-size: 13px;
  margin: 0 0 20px 0;
}

.footer-version {
  color: rgba(255, 255, 255, 0.6);
  font-size: 11px;
  margin: 0;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

/* Print Button */
.print-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 10px 25px -5px rgb(0 0 0 / 0.3);
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.3s;
  z-index: 1000;
  line-height: 1;
}

.print-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 15px 30px -5px rgb(0 0 0 / 0.4);
}

.print-btn:active:not(:disabled) {
  transform: translateY(0);
}

.print-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.print-btn i {
  font-size: 20px;
}

/* Print Styles */
@media print {
  * {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  
  .no-print {
    display: none !important;
  }
  
  body,
  .user-guide {
    background: white !important;
    margin: 0;
    padding: 0;
  }
  
  .container {
    max-width: 100%;
    padding: 0;
  }
  
  .main-content {
    padding: 0 !important;
  }
  
  .guide-header {
    padding: 20px;
    margin-bottom: 20px;
    border-bottom: 2px solid #10b981;
  }
  
  .section-card {
    page-break-inside: avoid;
    break-inside: avoid;
    box-shadow: none !important;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
    padding: 20px;
  }
  
  .content-box {
    page-break-inside: avoid;
    break-inside: avoid;
    margin-bottom: 15px;
    padding: 15px;
  }
  
  .problem-card,
  .feature-item {
    page-break-inside: avoid;
    break-inside: avoid;
  }
  
  h2, h3 {
    page-break-after: avoid;
  }
  
  /* Ensure backgrounds and colors print */
  .step-number,
  .badge-custom,
  .highlight-box,
  .tip-box {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .section-card {
    padding: 24px;
  }
  
  .content-box {
    padding: 20px;
  }
  
  .quick-ref-grid {
    grid-template-columns: 1fr;
  }
  
  .problem-grid {
    grid-template-columns: 1fr;
  }
  
  .print-btn {
    bottom: 16px;
    right: 16px;
    padding: 14px 20px;
    font-size: 14px;
  }
  
  .print-btn span {
    display: none;
  }
  
  .print-btn i {
    font-size: 24px;
  }
}
</style>
