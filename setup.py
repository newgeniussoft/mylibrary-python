from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    description='A simple math and string manipulation library',
    author='Gino',
    author_email='georgino197@gmail.com',
    url='https://github.com/newgeniussoft/mylibrary-python.git',  # replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
