# Standard library imports
import subprocess

def query_nvsmi(properties, index=None):
	query = ['nvidia-smi', '--query-gpu={}'.format(properties), '--format=csv,noheader,nounits']

	if index is not None:
		query.append('--id={}'.format(index))

	process = subprocess.Popen(query, stdout=subprocess.PIPE)

	return process.stdout.read().decode()

class GPU:
	def __init__(self, index, name, total_memory, uuid):
		self.index = int(index)
		self.name = name
		self.total_memory = int(total_memory)
		self.uuid = uuid

	def get_clock_speeds(self):
		output = query_nvsmi('clocks.gr,clocks.mem', self.index)
		columns = output.rstrip().split(', ')

		return {
			'core_clock_speed': int(columns[0]),
			'memory_clock_speed': int(columns[1])
		}

	def get_max_clock_speeds(self):
		output = query_nvsmi('clocks.max.gr,clocks.max.mem', self.index)
		columns = output.rstrip().split(', ')

		return {
			'max_core_clock_speed': int(columns[0]),
			'max_memory_clock_speed': int(columns[1])
		}

	def get_memory_details(self):
		output = query_nvsmi('memory.used,memory.free', self.index)
		columns = output.rstrip().split(', ')

		return {
			'used_memory': int(columns[0]),
			'free_memory': int(columns[1])
		}

def get_gpus():
	output = query_nvsmi('index,name,memory.total,uuid')
	gpus = []

	for line in output.splitlines():
		gpus.append(GPU(*line.split(', ')))

	return gpus

if __name__ == '__main__':
	for gpu in get_gpus():
		print(gpu.__dict__)
		print(gpu.get_max_clock_speeds())
		print(gpu.get_clock_speeds())
		print(gpu.get_memory_details())
