{
    "name": 'Purchase Request',
    "summary": "Added smart buttons in purchase order, purchase request and purchase rfq which connects all these 3 models for dallas.",
    "version": "17.0.0.0.0",
    "category": "Purchase",
    "author": "Biztras",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ['base', 'mail', 'product', 'account', 'purchase', 'base_tier_validation', 'sale'],
    "website": "https://biztras.com/",
    "data": [
        'security/ir.model.access.csv',
        'data/data.xml',
        'report/purchase_request_report.xml',
        'views/purchase_request.xml',
        'wizard/wizard_vendor_selection.xml'
    ],

}
