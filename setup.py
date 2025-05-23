from setuptools import setup, find_packages


def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='ML-Project',
    version='0.0.1',
    author='Kunal Naresh Kalkotwar',
    author_email='kunalkalkotwar21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)