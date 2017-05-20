"""Setup for string_repeat.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov',
                'test_most_digits.py', 'tox']
}

setup(
    name='most digits',
    desctription='Implements the most digits program.',
    version='0.1',
    author='Chris Hudson',
    author_email='c.ahudson84@yahoo.com',
    license='MIT',
    py_modules=['most_digits'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={
        'console_scriptes': [
            'mostdigits = mostdigits:main'
        ]
    }
)
