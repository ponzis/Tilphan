from distutils.core import setup

setup(
    name='Tilphan',
    version='0.0.01',
    packages=['tilphan'],
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
            'pytest>=3.6',
        ],
    }
)