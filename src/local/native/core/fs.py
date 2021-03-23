import os
import shutil
import tempfile

def _symlink_force(target, link_name):
  '''
  Create a symbolic link link_name pointing to target.
  Overwrites link_name if it exists.
  '''

  # os.replace() may fail if files are on different filesystems
  link_dir = os.path.dirname(link_name)

  while True:
    temp_link_name = tempfile.mktemp(dir=link_dir)
    try:
      os.symlink(target, temp_link_name)
      break
    except FileExistsError:
      pass
  try:
    os.replace(temp_link_name, link_name)
  except OSError:  # e.g. permission denied
    os.remove(temp_link_name)
    raise

def symlink(target, link_name, force=False):
  if force:
    return _symlink_force(target, link_name)
  return os.symlink(target, link_name)

def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
      shutil.copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)
