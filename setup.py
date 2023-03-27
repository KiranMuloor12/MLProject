from setuptools import find_packages, setup
from typing import List

hypen_e_dt = '-e .'

def get_requirements(file_path:str)->List[str]:
    #this function will return a list of requirements
    requirments=[]
    with open(file_path) as f:
        requirments=f.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if hypen_e_dt in requirments:
            requirments.remove(hypen_e_dt) 
    return requirments


setup(
    name='mlprojects',
    version='0.0.1',
    author='KiranMuloor',
    author_email='kiranchitra0612@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )