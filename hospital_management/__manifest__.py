{
    'name': 'Hospital Management',
    'version': '0.0.1',  # Versioning model major.minor.patch-fix
    'description': 'Manage Hospital patients data',
    'summary': 'Manage Hospital patients data',
    'author': 'Ahmed Khalifa',
    'website': 'https://micloud.nohost.me',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'depends': [
        'base','mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
    # 'demo': [
    #     ''
    # ],
    'auto_install': False,
    'application': True,
    'sequence': -98,
    # 'assets': {

    # }
}
