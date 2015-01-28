
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

# get the information between the calls
def string_between(s, first, last):
	start = s.index(first) + len(first)
	end = s.index(last, start)
	return s[start:end]

calls_information = []

for index in range(0, len(unformatted_calls)-1):
	calls_information.append(string_between(file_text, unformatted_calls[index], unformatted_calls[index+1]))

# still need to get the call information for the last call. Everything below the last call header

# members format
calls_members_pattern = re.compile(r"(\| )(?P<name>[\w]+)(.*)")
calls_members = re.findall(calls_members_pattern, file_text)

for call_member in calls_members:
	print call_member[1] + call_member[2]