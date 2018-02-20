# Standard library imports
import subprocess

# First-party imports
import base

def query_nvsmi(properties, index=None):
	query = ['nvidia-smi', '--query-gpu={}'.format(properties), '--format=csv,noheader,nounits']

	if index is not None:
		query.append('--id={}'.format(index))

	process = subprocess.Popen(query, stdout=subprocess.PIPE)
	output = process.stdout.read().decode()
	rows = []

	for line in output.splitlines():
		rows.append(line.rstrip().split(', '))

	return rows

class GPU(base.GPU):
	def __init__(self, index, name, total_memory):
		super().__init__(name, total_memory)
		self.index = int(index)

	def get_clock_speeds(self):
		row = query_nvsmi('clocks.gr,clocks.mem', self.index)[0]

		return {
			'core_clock_speed': int(row[0]),
			'memory_clock_speed': int(row[1])
		}

	def get_max_clock_speeds(self):
		row = query_nvsmi('clocks.max.gr,clocks.max.mem', self.index)[0]

		return {
			'max_core_clock_speed': int(row[0]),
			'max_memory_clock_speed': int(row[1])
		}

	def get_memory_details(self):
		row = query_nvsmi('memory.used,memory.free', self.index)[0]

		return {
			'used_memory': int(row[0]),
			'free_memory': int(row[1])
		}

def get_gpus():
	rows = query_nvsmi('index,name,memory.total')
	gpus = []

	for row in rows:
		gpus.append(GPU(*row))

	return gpus

if __name__ == '__main__':
	for gpu in get_gpus():
		print(gpu.__dict__)
		print(gpu.get_max_clock_speeds())
		print(gpu.get_clock_speeds())
		print(gpu.get_memory_details())
