from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete python dashboard miranda'
LONG_DESCRIPTION = 'Este es mi primer paquete de python y simula la gestion de un hotel'


setup(
        name="scripts", 
        version=VERSION,
        author="Omar Pérez",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'Faker 22.6.0',
            'mysql-connector-python 8.3.0',
            'pip 23.3.2',
            'pytest 7.4.4',
            'python-dotenv 1.0.1',
            'setuptools 69.0.3',
        ],
        entry_points={
        'console_scripts': [
            'create_db = seeds.create_db',
        ],
    },
)