"""Setup for Flight Paths."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox']
}

setup(
    name='Flight Paths',
    description='Python implementation of Flight paths code challenges.',
    version='0.1',
    author='Chris Hudson',
    author_email='c.ahudson84@yahoo.com',
    license='MIT',
    py_modules=['flight_paths'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
