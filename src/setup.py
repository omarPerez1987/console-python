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
            'Faker',
            'mysql-connector-python',
            'pip',
            'pytest',
            'python-dotenv',
            'setuptools',
        ],
)
