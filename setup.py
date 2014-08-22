from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='fleet_management',
    version=version,
    description='Managing Fleet and Vehicles',
    author='Dar Nazer Est.',
    author_email='dalwadani@darnazer.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
