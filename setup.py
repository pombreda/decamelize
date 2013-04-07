from setuptools import setup, find_packages

requires = [
    'distribute==0.6.36',
    'ipython==0.13.2',
    'py==1.4.13',
    'pytest==2.3.4'
    ]

setup(
        name='Decamelize',
        version='0.1',
        author='Chris Wolfe'
        author_email='cw@none.com' # fill in later
        description='Convert a camel cased project to one using underscores and caps to make it semi PEP-8 compliant'
        long_description=open('README.md').read()
        install_requires=requires
)
