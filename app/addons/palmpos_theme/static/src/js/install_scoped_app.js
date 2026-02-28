/** @odoo-module **/

import { InstallScopedApp } from "@web/core/install_scoped_app/install_scoped_app";
import { patch } from "@web/core/utils/patch";

patch(InstallScopedApp.prototype, {
    // No behavioral changes needed, just template override
});
