from setuptools import setup, find_packages

setup(
    name='AzurePythonConnectors',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='GPL',
    author='Srikanth Mohan',
    author_email='tmsrikanth1982@gmail.com',
    description='A package for connecting to various Azure services using Python.',
    install_requires=[
        'azure-identity',
        'azure-mgmt-resource',
        'azure-keyvault-secrets',
        'azure-storage-blob',
        'pyodbc'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)