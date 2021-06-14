import setuptools
import copy_files_and_search_max

with open('README.md') as fr:
    long_description = fr.read()

setuptools.setup(
    name='copy_files_and_search_max',
    version=copy_file_and_search_max.__version__,
    author='Shubenkov A.Y.',
    author_mail='shubenkov@tuta.io',
    desctiption='Copying files from a directory and finding the largest one',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Shubenkovll/copy_files_and_search_max',
    packages=setuptools.find_packages(),
    install_requires=[


    ],
    test_suite='tests',
    python_requires='>=3.9',
    platforms=["any"]
)









)
