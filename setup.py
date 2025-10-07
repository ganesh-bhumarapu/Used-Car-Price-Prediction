# from setuptools import find_packages, setup
# from typing import List

# # Constants
# HYPHEN_E_DOT = '-e .'

# def get_requirements(file_path: str) -> List[str]:
#     """
#     Returns the list of requirements from the given file path.

#     Args:
#     file_path (str): The path to the requirements file.

#     Returns:
#     List[str]: A list of requirements.
#     """
#     try:
#         with open(file_path, 'r') as file_obj:
#             requirements = file_obj.readlines()
#             requirements = [req.strip() for req in requirements]

#             # Remove '-e .' if present
#             if HYPHEN_E_DOT in requirements:
#                 requirements.remove(HYPHEN_E_DOT)

#             return requirements
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#         return []

# setup(
#     name='MLProject',
#     version='0.0.1',
#     author='Ganesh',
#     author_email='ganesh.bhumarapu@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file_obj:
            requirements = [req.strip() for req in file_obj.readlines()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
            return requirements
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

setup(
    name='MLProject',
    version='0.0.1',
    author='Ganesh',
    author_email='ganesh.bhumarapu@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt')
)
