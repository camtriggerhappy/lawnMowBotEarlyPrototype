from setuptools import find_packages
from setuptools import setup

setup(
    name='geometry_msgs',
    version='4.5.0',
    packages=find_packages(
        include=('geometry_msgs', 'geometry_msgs.*')),
)
