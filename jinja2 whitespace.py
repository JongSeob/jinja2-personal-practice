from pydoc import render_doc
from jinja2 import Template, Undefined, StrictUndefined


template = '''
Starting line
{# Just a comment #}                                  
Line after comment
'''

my_temp = Template(template, undefined=StrictUndefined)
rendered = my_temp.render()
print (rendered)

with open('whitespace_example.txt', 'w') as f:
    f.writelines(rendered)
print ('----------------------------------------------------')
template = '''
{% for iname, idata in interfaces.items() %}
interface {{ iname }}
 description {{ idata.description }}
  {% if idata.ipv4_address is defined %}
 ip address {{ idata.ipv4_address }}
  {% endif %}
{% endfor %}
'''
template_marked = '''
{% for iname, idata in interfaces.items() %} (1)
interface {{ iname }}
 description {{ idata.description }}
  {% if idata.ipv4_address is defined %} (2)
 ip address {{ idata.ipv4_address }}
  {% endif %} (3)
{% endfor %} (4)
'''
template_cleaned = '''
{%- for iname, idata in interfaces.items() -%}
interface {{ iname }}
 description {{ idata.description }}
  {% if idata.ipv4_address is defined -%}
 ip address {{ idata.ipv4_address }}
  {% endif -%}
{% endfor -%}
'''

data = {
  "interfaces": {
    "Ethernet2": {
      "ipv4_address": "10.50.0.0/31", 
      "description": "leaf01-eth51"
    }, 
    "Ethernet1": {
      "description": "capture-port"
    }
  }
}

my_temp = Template(template_marked, undefined=StrictUndefined)
print(my_temp.render(data))

my_temp = Template(template_cleaned, undefined=StrictUndefined)
print(my_temp.render(data))

### ** triming and lstrip 사용 시 whitespace 문제 해결 가능 **
## lstrip : block이 존재하는 line의 space, tab 문자를 모두 제거
## trim   : block 뒤쪽의 newline문자를 제거
my_temp = Template(template, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
print(my_temp.render(data))