try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='walkr',
    version='0.1',
    description='',
    author='The Mine',
    author_email='',
    url='',
    install_requires=[
        "Pylons>=1.0",
        "mysql-python>=1.2",
        "GeoAlchemy>=0.4.1",
        "SQLAlchemy>=0.6.0,<=0.6.99",
        "GeoAlchemy>=0.4.1",
        "Mako>=0.2.2,<=0.2.99",
        "FormBuild>=3.0,<3.99",
        "repoze.who>=1.0,<=1.0.99",
        "turbomail>=3.0.0,<=3.0.99"
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'walkr': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'walkr': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = walkr.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
