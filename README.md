fastQCorrector
==============

A simple Python command line tool for correcting invalid [fastq files](http://en.wikipedia.org/wiki/FASTQ_format "Fastq format") caused usually by truncation caused by error in gziping process.

The tool will drop incomplete or invalid sequencing read and output .fastq file that contains only the valid reads from the input.

## Dependency:

python 2.6 or up, default python modules:
gzip, argparse

## Installation:

```
	$ git clone https://github.com/wangz10/fastQCorrector.git
```

## Usage:

```
	$ python fastQCorrector.py [-h] fastq_filename
```
Since this script is written in native Python, one can also run with Pypy for faster run:
```
	$ pypy fastQCorrector.py [-h] fastq_filename
```
