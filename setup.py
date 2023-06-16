from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='The goal of this project is to predict how fit the candidates are based on their available information. The project is divided into 2 steps: Rank candidates based on a fitness score and then Re-rank candidates when a candidate is starred.',
    author='Dorcas Taiwo',
    license='MIT',
)
