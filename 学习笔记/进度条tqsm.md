# 进度条tqsm

###自动循环

```python
from tqdm import tqdm
for i in tqdm(range(10000)):
for i in ttrange(10000):
```

##观察处理的数据

通过`tqdm`提供的`set_description`方法可以实时查看每次处理的数据

```python
from tqdm import tqdm
import time

pbar = tqdm(["a","b","c","d"])
for c in pbar:
  time.sleep(1)
  pbar.set_description("Processing %s"%c)
```

## 手动循环

Manual control of `tqdm()` updates using a `with` statement:

```python
from tqdm import tqdm
import time

#total参数设置进度条的总长度
with tqdm(total=100) as pbar:
  for i in range(100):
    time.sleep(0.05)
    #每次更新进度条的长度
    pbar.update(1)
```

不使用==**with**==用完后要关闭，例如：==**pbar.close()**==

##多层循环进度条

通过`tqdm`也可以很简单的实现嵌套循环进度条的展示

```python
from tqdm import tqdm
import time

for i in tqdm(range(20), ascii=True,desc="1st loop"):
  for j in tqdm(range(10), ascii=True,desc="2nd loop"):
    time.sleep(0.01)
```

##pandas中使用tqdm

```python
import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))


tqdm.pandas(desc="my bar!")
df.progress_apply(lambda x: x**2)
```

在使用`tqdm`显示进度条的时候，如果代码中存在`print`可能会导致输出多行进度条，此时可以将`print`语句改为`tqdm.write`，代码如下

```python
for i in tqdm(range(10),ascii=True):
	tqdm.write("come on")
	time.sleep(0.1)
```





##不懂的地方-linux命令展示进度条

Perhaps the most wonderful use of `tqdm` is in a script or on the command line. Simply inserting `tqdm` (or `python -m tqdm`) between pipes will pass through all `stdin` to `stdout` while printing progress to `stderr`.

The example below demonstrate counting the number of lines in all Python files in the current directory, with timing information included.

```
$ time find . -name '*.py' -type f -exec cat \{} \; | wc -l
857365

real    0m3.458s
user    0m0.274s
sys     0m3.325s

$ time find . -name '*.py' -type f -exec cat \{} \; | tqdm | wc -l
857366it [00:03, 246471.31it/s]
857365

real    0m3.585s
user    0m0.862s
sys     0m3.358s
```

Note that the usual arguments for `tqdm` can also be specified.

```
$ find . -name '*.py' -type f -exec cat \{} \; |
    tqdm --unit loc --unit_scale --total 857366 >> /dev/null
100%|█████████████████████████████████| 857K/857K [00:04<00:00, 246Kloc/s]
```

Backing up a large directory?

```
$ tar -zcf - docs/ | tqdm --bytes --total `du -sb docs/ | cut -f1` \
  > backup.tgz
 44%|██████████████▊                   | 153M/352M [00:14<00:18, 11.0MB/s]
```

This can be beautified further:

```
$ BYTES="$(du -sb docs/ | cut -f1)"
$ tar -cf - docs/ \
  | tqdm --bytes --total "$BYTES" --desc Processing | gzip \
  | tqdm --bytes --total "$BYTES" --desc Compressed --position 1 \
  > ~/backup.tgz
Processing: 100%|██████████████████████| 352M/352M [00:14<00:00, 30.2MB/s]
Compressed:  42%|█████████▎            | 148M/352M [00:14<00:19, 10.9MB/s]
```

Or done on a file level using 7-zip:

```
$ 7z a -bd -r backup.7z docs/ | grep Compressing \
  | tqdm --total $(find docs/ -type f | wc -l) --unit files \
  | grep -v Compressing
100%|██████████████████████████▉| 15327/15327 [01:00<00:00, 712.96files/s]
```

Pre-existing CLI programs already outputting basic progress information will benefit from `tqdm`'s `--update` and `--update_to` flags:

```
$ seq 3 0.1 5 | tqdm --total 5 --update_to --null
100%|████████████████████████████████████| 5.0/5 [00:00<00:00, 9673.21it/s]
$ seq 10 | tqdm --update --null  # 1 + 2 + ... + 10 = 55 iterations
55it [00:00, 90006.52it/s]
```

