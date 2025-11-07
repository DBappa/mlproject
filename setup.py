from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requires(file_path:str) -> List[str]:
    '''returns the list of requirements'''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(

    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    author='bappa',
    author_email='bappadityadutta2024@gmail.com',
    install_requires=get_requires('requirements.txt')
)