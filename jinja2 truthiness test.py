from jinja2 import Template, Undefined, StrictUndefined

template = '''
{{ hostname }} is defined: {{ hostname is defined }}
{{ hostname }} is an iterable: {{ hostname is iterable }}
{{ hostname }} is a sequence: {{ hostname is sequence }}
{{ hostname }} is a string: {{ hostname is string }}

{{ eos_ver }} is a number: {{ eos_ver is number }}
{{ eos_ver }} is an integer: {{ eos_ver is integer }}
{{ eos_ver }} is a float: {{ eos_ver is float }}
{{ eos_ver }} is a iterable: {{ eos_ver is iterable }}

{{ bgp_as }} is a number: {{ bgp_as is number }}
{{ bgp_as }} is an integer: {{ bgp_as is integer }}
{{ bgp_as }} is a float: {{ bgp_as is float }}
{{ bgp_as }} is a iterable: {{ bgp_as is iterable }}

{{ interfaces }} is an iterable: {{ interfaces is iterable }}
{{ interfaces }} is a sequence: {{ interfaces is sequence }}
{{ interfaces }} is a mapping: {{ interfaces is mapping }}

{{ dns_servers }} is an iterable: {{ dns_servers is iterable }}
{{ dns_servers }} is a sequence: {{ dns_servers is sequence }}
{{ dns_servers }} is a mapping: {{ dns_servers is mapping }}
'''

data = {
    "hostname": "sw-office-lon-01",
    "eos_ver": 4.22,
    "bgp_as": 65001,
    "interfaces": {
        "Ethernet1": "Uplink to core"
    },
    "dns_servers": [
        "1.1.1.1",
        "8.8.4.4",
        "8.8.8.8"
    ]
}

my_temp = Template(template, undefined=StrictUndefined)
print (my_temp.render(data))