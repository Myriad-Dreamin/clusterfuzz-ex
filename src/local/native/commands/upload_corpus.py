
"""upload_corpus.py upload corpus to specific fuzzer."""

import os
import shutil
from local.native import fs

def find_fuzzer_type(fuzzer_name):
  fuzzer_name = fuzzer_name.lower()
  if 'libfuzzer' in fuzzer_name:
    return 'libfuzzer'
  return None

class LibfuzzerCorpusUploader(object):
  def __init__(self, args):
    pass
  
  def get_gcs_corpus_bucket(self, fuzzer_name):
    return os.path.join(os.environ['LOCAL_GCS_BUCKETS_PATH'], 'test-corpus-bucket', 'objects', 'libFuzzer', fuzzer_name)


corpus_uploaders = {
  'libfuzzer': LibfuzzerCorpusUploader,
}

def libfuzzer_get_fuzzer_corpus_bucket(args, ctrl, fuzzer_name):
  corpus_path = ctrl.get_gcs_corpus_bucket(fuzzer_name)
  fs.copytree(args.corpus, corpus_path, prefix='user-')

def execute(args):
  """upload corpus to specific fuzzer."""
  local_gcs_buckets_path = os.path.abspath(
      os.path.join(args.server_storage_path, 'local_gcs'))
  os.environ['LOCAL_GCS_BUCKETS_PATH'] = local_gcs_buckets_path

  fuzzer_type = find_fuzzer_type(args.fuzzer_name)
  if fuzzer_type not in corpus_uploaders:
    raise TypeError("fuzzer_type not found in args.fuzzer_name. it must be the substring of args.fuzzer_name")
  corpus_uploader_control = corpus_uploaders[fuzzer_type](args)
  libfuzzer_get_fuzzer_corpus_bucket(args, corpus_uploader_control, args.fuzzer_name)
