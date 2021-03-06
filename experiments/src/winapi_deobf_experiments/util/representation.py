
import numpy as np

from winapi_deobf_experiments.util.io import load_configs 

def interleave_lists(list_1, list_2, use_truncated_floats=True):
	if use_truncated_floats:
		if type(list_1[0]) is np.float64: #hacky; overly restrictive assumption 
			list_1=truncate_floats(list_1) #why not do in place?
		if type(list_2[0]) is np.float64: #hacky; overly restrictive assumption 
			list_2=truncate_floats(list_2) #can i do in place?
	return list(chain.from_iterable(izip(list_1, list_2))) #doesn't really seem "pythonic" but it's a one liner so...

def get_key_given_value(mydict,idx):
	key_name = mydict.keys()[mydict.values().index(idx)]
	return key_name 


def construct_configs(path_to_configs):
	"""

	Renders a yaml configs as a Bunch instance
	so that we can treat it like a class instance. 

	Arguments:
		path_to_configs: String.
			Filepath to configurations file.
	Returns:
		A Bunch instance representation of the configs. 
	"""
	configs = load_configs(path_to_configs)
	return Bunch(**configs) 



class Bunch:
	"""
	Transforms a dictionary into class attributes. 
		e.g. point = Bunch(datum=y, squared=y*y, coord=x)
	In my case I used this to load configs yaml file (loaded as a dictionary)
	into my class.  

	"""
	def __init__(self, **kwds):
		self.__dict__.update(kwds)