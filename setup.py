from setuptools import find_packages,setup
from typing import List



# getting requirements automatically in this file setup(install_requires)
def get_requirements(file_path:str)-> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        return requirements

setup(
    name="banglorepriceprediction",
    version='0.0.1',
    author='azhar',
    author_email='azharuddin.10121995@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


