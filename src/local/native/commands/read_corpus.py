
"""read_corpus.py read corpus from specific fuzzer."""

import os
from local.native import fs
from .ex_native_common import get_corpus_manager
import re

yellow = '\033[1;33m'
cyan = '\033[1;36m'
reset_color = '\033[0;0m'

def libfuzzer_read_from_fuzzer_corpus_bucket(args, ctrl, fuzzer_name):
  corpus_path = ctrl.get_gcs_corpus_bucket(fuzzer_name)
  corpus_all = os.listdir(corpus_path)
  total_num = len(corpus_all)
  regex_test = lambda _: True
  if args.prefix:
    regex_test = lambda s: s.startswith(args.prefix)
  elif args.pattern:
    regex_test = re.compile(args.pattern).match
  matched = []
  for corpus in corpus_all:
    if regex_test(corpus):
      matched.append(corpus)
  if len(matched) > args.limit:
    print(f"matched {len(matched)}, greater than limit {args.limit}")
  else:
    for corpus in matched:
      print(f"{cyan}>> beg of {yellow}{corpus}{cyan}...{reset_color}")
      with open(os.path.join(corpus_path, corpus), "r") as f:
        print(f.read())
      print(f"{cyan}>> end of {yellow}{corpus}{cyan}...{reset_color}")
    print(f"{len(matched)} of {total_num} corpus matched")

def execute(args):
  """read corpus from specific fuzzer."""
  local_gcs_buckets_path = os.path.abspath(
      os.path.join(args.server_storage_path, 'local_gcs'))
  os.environ['LOCAL_GCS_BUCKETS_PATH'] = local_gcs_buckets_path

  corpus_manager_control = get_corpus_manager(args.fuzzer_name)
  libfuzzer_read_from_fuzzer_corpus_bucket(args, corpus_manager_control, args.fuzzer_name)
