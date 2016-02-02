import json
""" 
This is a barebones Config parser for Haproxy. It is missing functionality for writing to
the config file and ensuring no duplicates exist for a specific setting.
"""
class ConfigParser(object):

	def __init__(self, config_file):
		self.config_file = open(config_file)
		self.json_obj = {}

	#Far simplar than a finite state machine but less extendable
	def parse_config(self):
		header = ""
		lines = self.config_file.readlines()
		for line in lines:
			if line.startswith((' ', '\t')) == False:
				header = line.strip()
				json_obj[header] = list()
				continue
			json_obj[header].append(line.strip())
	
	#Just returns the python dictionary containing settings as a json object to send from an API endpoint
	def config_to_json(self):
		return json.dumps(self.json_obj)
	
	#TODO: confirm if this is needed 
	def json_to_config(self):
		pass
	
	#TODO: confirm if this is needed
	def write_config(self):
		pass
	