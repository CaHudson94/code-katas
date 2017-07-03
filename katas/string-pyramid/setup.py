"""Setup for String Pyramid."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox']
}

setup(
    name='String Pyramid',
    description='Python implementation of string pyramid code challenges.',
    version='0.1',
    author='Chris Hudson',
    author_email='c.ahudson84@yahoo.com',
    license='MIT',
    py_modules=['string_pyramid'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
