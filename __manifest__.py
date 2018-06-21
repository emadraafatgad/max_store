{
    'name' : 'MAX STORE',
    'version' : '1.0',
    'summary': 'sales for shop ',
    'description': """
        how to make reatail system 
    """,
    'category': 'Retail',
    'website': 'http://www.emad.acme',
    'depends' : ['account', 'purchase', 'sale'],
    'data': [
        'views/retail_product.xml',
        'views/retail_product_line.xml',
        'views/retail_sale.xml',
        'views/retail_purchase.xml',
        'views/retail_inventory.xml',
        'views/retail_sale_order.xml',
        'views/retail_partner.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'sequence':2
}
