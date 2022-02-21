from jinja2 import StrictUndefined, Template, Undefined
import jinja2

template = '''
{% for i in  sflow_boxes|batch(2) %}
Sflow group{{ loop.index }}: {{ i | join(', ') }}
{% endfor %}
'''

data = {
  "sflow_boxes": [
    "10.180.0.1", 
    "10.180.0.2", 
    "10.180.0.3", 
    "10.180.0.4", 
    "10.180.0.5"
  ]
}

tmpl = jinja2.Template(template, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
print (tmpl.render(data))

template = '''
{% if eos_ver | float >= 4.22 %}
Detected EOS ver {{ eos_ver }}, using new command syntax.
{% else %}
Detected EOS ver {{ eos_ver }}, using old command syntax.
{% endif %}
'''

data = {'eos_ver': '4.10'}

tmpl = jinja2.Template(template, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
print (tmpl.render(data))