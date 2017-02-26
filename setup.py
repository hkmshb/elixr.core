import os
import elixr
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()


requires = []
tests_requires = [
    'pytest',
    'pytest-cov'
]

setup(
    name='elixr',
    version=elixr.__version__,
    description='A python general purpose utility library',
    long_description=README + '\n\n' + CHANGES,
    author=elixr.__author__,
    author_email='info@hazeltek.com',
    maintainer='Abdul-Hakeem Shaibu',
    maintainer_email='hkmshb@gmail.com',
    url='https://bitbucket.org/hkmshb/elixr',
    keywords='elixr, hazeltek elixr',
    zip_safe=False,
    packages=find_packages(),
    platforms='any',
    install_requires=requires,
    extras_require={ 'testing': tests_requires },
    classifiers=[
        'Development Status :: *',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: ISV',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ]
)