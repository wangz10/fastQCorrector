import argparse as ap
import gzip


def _fastQVlidator(lines):
	nucleotides = set(['A','T','C','G'])
	assert len(lines) == 4
	assert lines[0].startswith('@')
	assert set(lines[1]) | nucleotides == nucleotides
	assert set(lines[2]).startswith('+')
	assert len(lines[3]) == len(lines[1])


def _readFourLines(f):	
	f = iter(f)
	while True:
		lines = [None] * 4
		for i in range(4):
			try:
				lines[i] = f.next()
			except StopIteration:
				return
		try:
			_fastQVlidator(lines)
			yield lines
		except AssertionError:
			next(f)
			_readFourLines(f)


def correcter(f, outfn):
	# f is the handle of .fastq file or .fastq.gz file
	with open (outfn, 'wb') as out:
		for lines in _readFourLines(f):
			out.write(lines)
	return


def main():
	parser = ap.ArgumentParser()
	parser.add_argument('fastq filename', help='the name of the fastq file', type=str)
	args = vars(parser.parse_args())
	fastq_fn = args['fastq filename']
	outfn = fastq_fn.split('.fastq')[0] + '_fixed.fastq'
	if fastq_fn.endswith('.gz'):
		with gzip.open (fastq_fn) as f:
			correcter(f, outfn)
	elif fastq_fn.endswith('.fastq'):
		with open (fastq_fn) as f:
			correcter(f, outfn)
	else:
		raise IOError('Unrecognizable file extention in file: %s'%fastq_fn)


if __name__ == '__main__':
	main()
