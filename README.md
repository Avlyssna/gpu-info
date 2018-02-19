# gpu-info
Need GPU information? Don't sweat it; we've got your back.

## Installation
We're living in the future, man. Just `pip install gpu-info` and you're set!

## Usage
You're probably wondering how it works; let me explain. It's so simple, that it's **simple**. That's how simple it gets.

```python
import gpuinfo

for gpu in gpuinfo.get_gpus():
	print(gpu.__dict__)
	print(gpu.get_clock_speeds())
	print(gpu.get_memory_details())
```

That's all there is to it. **Simple**, huh?
