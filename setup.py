from setuptools import setup, find_packages

setup(
    name='helloer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Manav',
    author_email='manavchavda594@gmail.com',
    description='A simple greeting package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/drstoneml/helloer',
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
