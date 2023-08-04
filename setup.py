from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requriments(file_path:str)->List[str]:
    requrments=[]
    with open(file_path) as file_obj:
        requrments=file_obj.readlines()
        requrments=[req.replace("\n","") for req in requrments]
        return requrments
setup(
    name="DimondPrice",
    version='0.0.1',
    author='Abhyudaya',
    author_email='abhyudayadev123@gmail.com',
    install_requires=get_requriments('requirments.txt'),
    packages=find_packages()
    ##

)
