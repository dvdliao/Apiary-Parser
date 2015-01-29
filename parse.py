
import re

INPUT = "apiary.txt"

input_file = open(INPUT)
file_text = input_file.read()
input_file.close()

# Extracting call name and type

api_calls_pattern = re.compile(r"(#{3} )(?P<name>[\w\s]*)\[?(?P<type>[\w]+)\]?")
api_calls_pattern_unformatted = re.compile(r"(#{3})(.+)", re.MULTILINE)

api_calls = re.findall(api_calls_pattern, file_text)
unformatted_api_calls = re.findall(api_calls_pattern_unformatted, file_text)

calls = map(lambda x: x[1], api_calls)
unformatted_calls = map(lambda x: ''.join(x), unformatted_api_calls)

# for call in calls:
# 	print call

# get the information between the calls
def string_between(s, first, last):
	start = s.index(first) + len(first)
	end = s.index(last, start)
	return s[start:end]

calls_information = []

for index in range(0, len(unformatted_calls)-1):
	calls_information.append(string_between(file_text, unformatted_calls[index], unformatted_calls[index+1]))

# still need to get the call information for the last call. Everything below the last call header

calls_members = re.findall(r"(\| [\w\s|]+)+", file_text)

calls_members = map(lambda x: re.sub(r"( +)",r" ", x), calls_members) # reduce multiple spaces down to one
calls_members = map(lambda x: re.sub(r"\n",r"", x), calls_members) # remove all \n characters
calls_members = map(lambda x: x.split("|"), calls_members)
calls_members = map(lambda x: filter(None, x), calls_members) #remove all empty strings

# for cm in calls_members:
# 	print cm