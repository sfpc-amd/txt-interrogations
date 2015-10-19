import sys
import re

def setup(path1, path2):
	print(path1, path2);
	dict1 = dict_from_dialogue_path(path1)
	# dict2 = dict_from_dialogue_path(path2)
	print(dict1)


def dict_from_dialogue_path(path):

	character_re = re.compile("^([A-Z ]{3,})\s?(\([A-Z. ]+\))?")

	# this will store character names
	characters = {}
	last_pair = []
	character_name = ''

	for item in open(path):
			# check if title is uppercase
			# if it is uppercase
			line = item.strip()
			words = item.split()


			if len(words) > 0:
				if words[0].isupper():
					character_name = get_name(item)
					last_pair = [item]
				else:
					last_pair.append(item)
					if character_name in characters:
						characters[character_name].append(last_pair)
					else:
						characters[character_name] = [last_pair]

	return characters
			

def get_name(s):
	return s


if len(sys.argv) > 1:
	setup(sys.argv[1], sys.argv[2])

