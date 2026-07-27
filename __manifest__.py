{
    'name': 'Purchase Payment Workflow',
    'version': '1.0',
    'depends': ['purchase', 'account', 'stock'],
    'data': [
        "views/purchase_order_views.xml",
        "views/stock_picking_views.xml",

    ],
    'installable': True,
    'application': False,
}