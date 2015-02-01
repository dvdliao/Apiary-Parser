import re

INPUT = "apiary.txt"

input_file = open(INPUT)
file_text = input_file.read()
input_file.close()

# Extracting call name and type

api_calls_name_pattern = re.compile(r"(#{3} )(?P<name>[\w\s]*)\[?(?P<type>[\w]+)\]?\n*.*\n.*\n.*(?P<header>[\n \w.:;/\-\=\"]*)\n*.*\n.*\n.*(?P<body>[\n \w.:;/\-\=\"\{\}\[\]\'\,#]*)")
api_calls_name_pattern_unformatted = re.compile(r"(#{3})(.+)", re.MULTILINE)

api_calls = re.findall(api_calls_name_pattern, file_text)
unformatted_api_calls = re.findall(api_calls_name_pattern_unformatted, file_text)

calls_name = map(lambda x: x[1], api_calls)
calls_method = map(lambda x: x[2], api_calls)
calls_header = map(lambda x: x[3], api_calls)
calls_body = map(lambda x: x[4], api_calls)

unformatted_calls = map(lambda x: ''.join(x), unformatted_api_calls)

for name, method, header, body in zip(calls_name, calls_method, calls_header, calls_body):
	with open(name + ".json", 'w') as output_json_file:
		output_json_file.write("{\"method\": " + "\"" + method + "\"" + "}\n")
		output_json_file.write("{\"headers\": " + "\"" + header + "\"" + "}\n")
		output_json_file.write(body);



