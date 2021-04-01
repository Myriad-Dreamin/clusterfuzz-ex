
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
	parser_upload_corpus.add_argument(
			'--validate_fuzzer', help='path to the fuzzer.')
	# parser_upload_corpus.add_argument(
	#     'log_names', nargs='+', help='The log file names (without .log).')


	parser_read_corpus = subparsers.add_parser(
			'read_corpus',
			help=('read corpus from specific fuzzer'))
	parser_read_corpus.add_argument(
			'--server-storage-path',
			default='local/storage',
			help='Server storage path.')
	parser_read_corpus.add_argument(
			'--fuzzer_name', help='Name of the fuzzer.', required=True)
	parser_read_corpus.add_argument(
			'--prefix', help='filter with prefix string.', default='')
	parser_read_corpus.add_argument(
			'--pattern', help='filter with pattern string.', default='')
	parser_read_corpus.add_argument(
			'--limit', type=int, help='Read Limit.', default=5)


	parser_run_fuzz_bot = subparsers.add_parser(
		'run_fuzz_bot', help='Run a local clusterfuzz bot.')
	parser_run_fuzz_bot.add_argument(
		'--name', default='test-bot', help='Name of the bot.')
	parser_run_fuzz_bot.add_argument(
		'--fuzz-job', default='', help='Enforce the fuzz job to run')
	parser_run_fuzz_bot.add_argument(
		'--server-storage-path',
		default='local/storage',
		help='Server storage path.')
	parser_run_fuzz_bot.add_argument('directory', help='Directory to create bot in.')
	parser_run_fuzz_bot.add_argument(
		'--android-serial',
		help='Serial number of an Android device to connect to instead of '
		'running normally.')
	return parser

if __name__ == '__main__':
    butler._ArgumentParser = _ArgumentParser
    butler.main()
