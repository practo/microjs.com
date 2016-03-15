FILES = ['/home/ubuntu/www/consumer-payments-web/views/layout.jade', '/home/ubuntu/www/consumer-payments-web/views/admin/adminLayout.jade']

import json

def get_entry(name):
    output_template = {
        'name': name,
        'version': "",
        'github': "",
        'tags': ["consumer payments"],
        'description': "",
        'url': "",
        'source': ""
    }
    return output_template

output = set([])

def process(fname):
    with open(fname, 'r') as f:
        for line in f:
            if 'script(src=' in line:
                name = line.split('/')[-1].replace('")', '').strip()
                entry = json.dumps(get_entry(name), indent=4, sort_keys=True)
                output.add(entry)

for f in FILES:
    process(f)

print(','.join(list(output)))
