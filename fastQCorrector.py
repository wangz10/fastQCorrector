import argparse as ap
import gzip


def _fastQVlidator(lines):
	## asserting the reads (4 consecutive lines of fastq file)
	assert lines[0].startswith('@')
	assert lines[2].startswith('+')
	assert len(lines[3]) == len(lines[1])


def _readFourLines(f):
	## a four-line window for reading fastq file
	while True:
		lines = [None] * 4
		for i in range(4):
			try:
				lines[i] = next(f)
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
	with gzip.open (outfn, 'wb') as out:
		for lines in _readFourLines(f):
			out.write(''.join(lines))
	return


def main():
	parser = ap.ArgumentParser()
	parser.add_argument('fastq filename', help='the name of the fastq file', type=str)
	args = vars(parser.parse_args())
	fastq_fn = args['fastq filename']
	outfn = fastq_fn.split('.fastq')[0] + '_fixed.fastq.gz'
	print 'output is being written in %s' % outfn
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
