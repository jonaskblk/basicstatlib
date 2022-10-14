from setuptools import find_packages, setup

setup(
    name='basicstatlib',
    packages=find_packages(include=['basicstatlib']),
    version='0.1.0',
    description='A basic statistic library',
    author='Jonas Kubelke',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==2.11.1'],
    tests_require=['pytest==7.1.1'],
    test_suite='test_basicstatlib',
)