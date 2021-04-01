
import os
import shutil
import src.local.native.core.fs as fs

join = os.path.join
abspath = os.path.abspath
abs_join = lambda *args: abspath(join(*args))

local_clusterfuzz_root_dir = abspath(".")
clusterfuzz_root_dir  = abspath("../clusterfuzz")

import sys
sys.path.insert(0, abs_join(clusterfuzz_root_dir, 'src'))

# guard needs to be at the top because it checks Python dependecies.
from local.butler import guard
try:
  guard.check()
except Exception as e:
  if not e.args: 
      e.args=tuple()
  e.args = e.args + (f"raised by clusterfuzz, follow clusterfuzz's ({clusterfuzz_root_dir}) advice to pass the guard check",)
  raise

# python butler.py run_server
if __name__ == '__main__':
  butler_ex = abs_join(local_clusterfuzz_root_dir, "src/butler_ex.py")
  butler_ex_target = abs_join(clusterfuzz_root_dir, "butler_ex.py")
  shutil.copy2(butler_ex, butler_ex_target)

  local_native_commands_dir = abs_join(local_clusterfuzz_root_dir, "src/local/native/commands")
  butler_commands_dir = abs_join(clusterfuzz_root_dir, "src/local/butler")
  fs.copytree(local_native_commands_dir, butler_commands_dir)

  local_native_core_dir = abs_join(local_clusterfuzz_root_dir, "src/local/native/core")
  core_dir = abs_join(clusterfuzz_root_dir, "src/local/native")
  fs.symlink(local_native_core_dir, core_dir, force=True)

  # local_native_patch_dir = abs_join(local_clusterfuzz_root_dir, "src/local/native/patch")
  # patch_dir = abs_join(clusterfuzz_root_dir, "src/local/native/patch")
  # fs.symlink(local_native_patch_dir, patch_dir, force=True)
