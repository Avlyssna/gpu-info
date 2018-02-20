# gpu-info
Need GPU information? Don't sweat it; we've got your back.

## Installation
We're living in the future, man. Just `pip install gpu-info` and you're set!

## Usage
You're probably wondering how it works; let me explain. It's so simple, that it's **simple**. That's how simple it gets.

```python
from gpuinfo.nvidia import get_gpus

for gpu in get_gpus():
	print(gpu.__dict__)
	print(gpu.get_max_clock_speeds())
	print(gpu.get_clock_speeds())
	print(gpu.get_memory_details())
```

But let's say you don't want to rely on NVSMI. Let's say you want a solution that's built in to Windows and works with AMD cards. Well, we have the solution for you!

```python
from gpuinfo.windows import get_gpus

for gpu in get_gpus():
	print(gpu.__dict__)
```

And that's all there is to it. **Simple**, huh?
