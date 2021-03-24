
"""upload_corpus.py upload corpus to specific fuzzer."""

import os
from local.native import fs
from .ex_native_common import get_corpus_manager

def libfuzzer_upload_to_fuzzer_corpus_bucket(args, ctrl, fuzzer_name):
  corpus_path = ctrl.get_gcs_corpus_bucket(fuzzer_name)
  fs.copytree(args.corpus, corpus_path, prefix='user-')

def execute(args):
  """upload corpus to specific fuzzer."""
  # validate_fuzzer = None
  # if args.validate_fuzzer:
  #   validate_fuzzer = os.abspath(args.validate_fuzzer)
  # print('validate_fuzzer', args.validate_fuzzer)
  local_gcs_buckets_path = os.path.abspath(
      os.path.join(args.server_storage_path, 'local_gcs'))
  os.environ['LOCAL_GCS_BUCKETS_PATH'] = local_gcs_buckets_path

  corpus_manager_control = get_corpus_manager(args.fuzzer_name)
  libfuzzer_upload_to_fuzzer_corpus_bucket(args, corpus_manager_control, args.fuzzer_name)
