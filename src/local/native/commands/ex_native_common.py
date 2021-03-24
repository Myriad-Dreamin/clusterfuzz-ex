
import os

def find_fuzzer_type(fuzzer_name):
  fuzzer_name = fuzzer_name.lower()
  if 'libfuzzer' in fuzzer_name:
    return 'libfuzzer'
  return None

class LibfuzzerCorpusManager(object):
  def __init__(self):
    pass
  
  def get_gcs_corpus_bucket(self, fuzzer_name):
    return os.path.join(os.environ['LOCAL_GCS_BUCKETS_PATH'], 'test-corpus-bucket', 'objects', 'libFuzzer', fuzzer_name)


corpus_managers = {
  'libfuzzer': LibfuzzerCorpusManager,
}

def get_corpus_manager(fuzzer_name):
  fuzzer_type = find_fuzzer_type(fuzzer_name)
  if fuzzer_type not in corpus_managers:
    raise TypeError("fuzzer_type not found in fuzzer_name. it must be the substring of fuzzer_name")
  return corpus_managers[fuzzer_type]()
