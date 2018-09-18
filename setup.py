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
        "testing": [
            "pytest >= 3.0.0, <4",
            "pytest-cov >= 2.5.1, <3",
            "pytest-mock >= 1.10.0, <2",
            "pytest-timeout >= 1.3.0, <2",
            "pytest-xdist >= 1.22.2, <2",
            "pytest-randomly >= 1.2.3, <2",
        ],
        'docs': [
            'sphinx>=1.7.4',
            'sphinxcontrib-asyncio',
            'sphinxcontrib-websupport',
        ]
    }

)
