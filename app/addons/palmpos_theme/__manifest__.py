{
    'name': 'PalmPOS Theme',
    'version': '19.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Custom CSS styles for PalmPOS',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'palmpos_theme/static/src/css/palmpos.css',
        ],
        'point_of_sale._assets_pos': [
            'palmpos_theme/static/src/css/pos_branding.css',
        ],        
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
