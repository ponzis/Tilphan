from setuptools import setup

setup(
    name='Tilphan',
    version='',
    packages=['tilphan'],
    url='',
    license='',
    author='Ponzis',
    author_email='',
    description='',
    python_requires='>=3.5.3',
    install_requires=[
        'discord.py[voice]>=0.16.12',

    ],
    extras_require={
        'docs': [
            'sphinx>=1.7.4',
            'sphinxcontrib-asyncio',
            'sphinxcontrib-websupport',
        ]
    }

)
