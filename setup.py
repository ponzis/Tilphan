from setuptools import setup

setup(
    name='Tilphan',
    version='0.0.1',
    packages=['tilphan', 'tests'],
    url='',
    license='',
    author='Ponzis',
    author_email='',
    description='',
    extras_require={
        'docs': [
            'sphinx',
            'sphinx_rtd_theme',
        ],
        'testing': [
            'pytest',
        ],
    }
)