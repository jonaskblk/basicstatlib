from setuptools import find_packages, setup

setup(
    name='qlib',
    packages=find_packages(include=['qlib']),
    version='0.0.1',
    description='A basic data science library',
    author='Jonas Kubelke',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==2.11.1'],
    tests_require=['pytest==7.1.1'],
    test_suite='test_qlib',
    package_dir={'':'qlib'}
)