from distutils.core import setup

setup(
    name='crime-in-sc-flask',
    version='0.1dev',
    packages=['src', 'src.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    # entrypoints={
    #     'console_scripts': [
    #         'run=src.main:main',
    #     ],
    # },

    install_requires=[
        'pytest>=7.2.2',
        'requests>=2.28.2',
        'pandas>=1.3.5',
        'flask>=2.2.3',
        'gunicorn>=21.2.0'

    ]
)
