from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'random',
        'unittest'
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package_name.your_module_name:main',
        ],
    },
    author='Fatemeh Salimi',
    author_email='fatemeh.sbrn@gmail.com',
    description='homework',
    url='https://github.com/salimiftmh/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
