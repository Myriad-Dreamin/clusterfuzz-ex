
# ClusterFuzz-Ex

### Extend upstream python code

```shell
in /path/to/clusterfuzz
 $ python -m pip_env shell
in /path/to/clusterfuzz
 (clusterfuzz-virtual-env) $ cd ../clusterfuzz-ex
in /path/to/clusterfuzz-ex
 (clusterfuzz-virtual-env) $ python extend_upstream.py
```

### Verify extension

```shell
in /path/to/clusterfuzz
 (clusterfuzz-virtual-env) $ $ python butler_ex.py --help
usage: butler_ex.py [-h] {upload_corpus,bootstrap,...}
...
```
