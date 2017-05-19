"""Setup for string_repeat.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov',
                'test_string_repeat.py', 'tox']
}

setup(
    name='stringrepeat',
    desctription='Implements the Mail program.',
    version='0.1',
    author='Chris Hudson, James Feore, Sean Beseler',
    author_email='c.ahudson84@yahoo.com, bob@bob.com, seanwbeseler@gmail.com',
    license='MIT',
    py_modules=['mail'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={
        'console_scriptes': [
            'stringrepeat = stringrepeat:main'
        ]
    }
)
