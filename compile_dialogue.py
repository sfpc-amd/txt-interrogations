import sys
import re
import random

def setup(path1, path2):
	# print(path1, path2);
	dict1 = dict_from_dialogue_path(path1)
	dict2 = dict_from_dialogue_path(path2)
	allDialogue = dict1.copy()
	allDialogue.update(dict2);

	questions = get_questions(dict2)
	answers = get_answers(dict1)

	n = 6
	questions_sample = random.sample(questions['JORDAN'], n)
	answers_sample = random.sample(answers['GATSBY'], n)



	for i, question in enumerate(questions_sample):
		print(question['character_name'])
		print(question['dialogue'])
		answer = answers_sample[i]
		print(answer['character_name'])
		print(answer['dialogue'])

	# print("JORDAN: "+random.choice(questions['JORDAN'])['dialogue'])

	# for k, v in allDialogue.iteritems():
		# print(k, v)


def get_answers(d):
	answers = {}

	for k, v in d.iteritems():
		for item in v:
			lines = " ".join(item['dialogue_lines'])
			if lines.find('?') == -1:
				if k in answers:
					answers[k].append(item)
				else:
					answers[k] = [item]

	return answers

def get_questions(d):
	questions = {}

	for k, v in d.iteritems():
		for item in v:
			lines = "".join(item['dialogue_lines'])
			if lines.find('?') > -1:
				if k in questions:
					questions[k].append(item)
				else:
					questions[k] = [item]

	return questions

def dict_from_dialogue_path(path):

	character_re = r'^([A-Z ]{3,})\s?(\([A-Z. ]+\))?\s?$'

	# this will store character names
	characters = {}
	data = {}
	character_name = ''

	for item in open(path):
			line = item.strip()
			words = line.split()

			# if there is anything in the line
			if len(words) > 0:

				# check if it's a character name
				m = re.match(character_re, line)

				# if not, add lines to current character

				if m:
					# save the current one
					if 'character_name' in data:
						characters = add_character(data['character_name'], data, characters)

					# create a new character
					data = new_character(line, m)

				# otherwise, we are starting a new character
				else:
					if 'dialogue_lines' in data:
						data['dialogue_lines'].append(line)
						# join and set dialogue
						data['dialogue'] = " ".join(data['dialogue_lines'])
	


	return characters


def add_character(name, data, dictionary):
	if name in dictionary:
		dictionary[name].append(data)
	else:
		dictionary[name] = [data]

	return dictionary

def new_character(line, m):
	data = {}
	character_name = m.group(1).strip(' \n')
	data['character_name'] = character_name

	data['character_detail'] = ''
	data['character_original'] = line
	data['dialogue_lines'] = []
	data['dialogue'] = ''

	if m.group(2):
		 data['character_detail'] = m.group(2).strip("()/n")

	return data


if len(sys.argv) > 1:
	setup(sys.argv[1], sys.argv[2])

