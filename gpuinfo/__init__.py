# Standard library imports
import subprocess

def query_nvsmi(properties, index=None):
	query = ['nvidia-smi', '--query-gpu={}'.format(properties), '--format=csv,noheader,nounits']

	if index is not None:
		query.append('--id={}'.format(index))

	process = subprocess.Popen(query, stdout=subprocess.PIPE)

	return process.stdout.read().decode()

class GPU:
	def __init__(self, index, name, uuid):
		self.index = int(index)
		self.name = name
		self.uuid = uuid

	def get_clock_speeds(self):
		output = query_nvsmi('clocks.gr,clocks.mem', self.index)
		columns = output.rstrip().split(', ')

		return {
			'core_clock_speed': int(columns[0]),
			'memory_clock_speed': int(columns[1])
		}

	def get_memory_details(self):
		output = query_nvsmi('memory.total,memory.used,memory.free', self.index)
		columns = output.rstrip().split(', ')

		return {
			'total_memory': int(columns[0]),
			'used_memory': int(columns[1]),
			'free_memory': int(columns[2])
		}

def get_gpus():
	output = query_nvsmi('index,name,uuid')
	gpus = []

	for line in output.splitlines():
		gpus.append(GPU(*line.split(', ')))

	return gpus

if __name__ == '__main__':
	for gpu in get_gpus():
		print(gpu.__dict__)
		print(gpu.get_clock_speeds())
		print(gpu.get_memory_details())
