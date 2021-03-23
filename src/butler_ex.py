
import butler

butler_parser = butler._ArgumentParser
# print(butler_parser)

def _ArgumentParser(*args, **kwargs):
	parser = butler_parser(*args, **kwargs)

	subparsers = parser.add_subparsers(dest='command')
	prev_add_subparsers = parser.add_subparsers
	parser.add_subparsers = lambda *_, **kwargs: subparsers if kwargs['dest'] == 'command' else prev_add_subparsers(*_, **kwargs)
	parser_upload_corpus = subparsers.add_parser(
			'upload_corpus',
			help=('Upload corpus to specific fuzzer'))
	parser_upload_corpus.add_argument(
			'--server-storage-path',
			default='local/storage',
			help='Server storage path.')
	parser_upload_corpus.add_argument(
			'--fuzzer_name', help='Name of the fuzzer.', required=True)
	parser_upload_corpus.add_argument(
			'--corpus', help='Corpus directory (or zipped directory) to add.', required=True)
	# parser_upload_corpus.add_argument(
	#     'log_names', nargs='+', help='The log file names (without .log).')
	return parser

if __name__ == '__main__':
    butler._ArgumentParser = _ArgumentParser
    butler.main()
