FILES = ['/home/ubuntu/www/chronosui/bower.json']

import json


def get_entry(name, version):
    output_template = {
        'name': name,
        'version': version,
        'github': "",
        'tags': ["chronos"],
        'description': "",
        'url': "",
        'source': ""
    }
    return output_template

output = set([])

def process(fname):
    with open(fname, 'r') as f:
        j = json.loads(f.read())
        for key, value in j['dependencies'].iteritems():
            output.add(json.dumps(get_entry(key, value), indent=4, sort_keys=True))

for f in FILES:
    process(f)

print(','.join(list(output)))
