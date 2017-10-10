import sys
import re
import json

get_option = re.compile(r'<option value="(.*?)">(.*?)</option>')

with open(sys.argv[1], 'r') as f:
    d = {}
    for key, value in get_option.findall(f.read()):
        d[key] = value

print(json.dumps(d, indent=4))
