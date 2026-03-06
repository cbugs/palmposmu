/** @odoo-module **/

import { InstallScopedApp } from "@web/core/install_scoped_app/install_scoped_app";
import { patch } from "@web/core/utils/patch";

patch(InstallScopedApp.prototype, {
    setup() {
        super.setup(...arguments);
        // Redirect to scoped app URL with PalmPOS parameters
        window.location.href = '/scoped_app?app_id=point_of_sale&app_name=PalmPOS';
    }
});
