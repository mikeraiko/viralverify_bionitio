#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='viralverify_bionitio',
    version='0.1.0.0',
    author='Mikhail Raiko',
    author_email='mraiko@eng.ucsd.edu',
    packages=['viralverify_bionitio'],
    package_dir={'viralverify_bionitio': 'viralverify_bionitio'},
    entry_points={
        'console_scripts': ['viralverify_bionitio = viralverify_bionitio.viralverify_bionitio:main']
    },
    url='https://github.com/mikeraiko/viralverify_bionitio',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
