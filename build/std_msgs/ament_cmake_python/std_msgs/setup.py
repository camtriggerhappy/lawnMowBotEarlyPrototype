from setuptools import find_packages
from setuptools import setup

setup(
    name='std_msgs',
    version='4.5.0',
    packages=find_packages(
        include=('std_msgs', 'std_msgs.*')),
)
