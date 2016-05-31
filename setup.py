import distutils.core

# TODO: Make sure that the packages are correctly setup
distutils.core.setup(
    name='SekPythonApi',
    version='1.0.0',
    install_requires=['Django', 'djangorestframework', 'django-filter', 'django-rest-swagger', 'markdown', 'psycopg2', 'djangotoolbox'],
    url='',
    license='GNU General Public License v3.0',
    author='Sung Eun Kim',
    author_email='kse0417@hotmail.com',
    description=''
)
