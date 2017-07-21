"""Setup for string_repeat.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov',
                'test_complimentary_dna.py', 'tox']
}

setup(
    name='Complimentary DNA',
    desctription='Implements the complimentary dna program.',
    version='0.1',
    author='Chris Hudson',
    author_email='c.ahudson84@yahoo.com',
    license='MIT',
    py_modules=['complimentary_dna'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={
        'console_scriptes': [
            'complimentarydna = complimentarydna:main'
        ]
    }
)
