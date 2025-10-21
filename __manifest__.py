{
    'name': 'Laporan Penjualan Tags',
    'version': '1.0.0',
    'summary': 'Menambahkan kolom Tags pada laporan Sales Analysis.',
    'author': 'Fakhrul Rosyid',
    'category': 'Sales',
    'depends': [
        'sale_management',
        'pos_sale',
        'crm',
    ],
    'data': [
        # 'security/ir.model.access.csv', # Dinonaktifkan sementara
        'views/sale_analysis_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}