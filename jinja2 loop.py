# loop and conditional
# 1. List Data Loop
# 2. Looping Over Dictionaries
# 3. items()를 활용한 dictionary access 코드 간소화

from jinja2 import StrictUndefined, Template, Undefined

# 1. List Data Loop
print ("========================")
print ("List Data Loop")
print ("========================")
template = """ Title
{#- permit은 permits list의 원소 #}
{%- for permit in permits %}
 {{ permit -}}
{% endfor %}
"""

# Hash pointing a List
data = {"permits":
        ["permit 1", "permit 2", "permit 3", "permit 4"]
        }
# YAML Style.
# PL_AS_65003_IN:
#   - permit 10.96.0.0/24
#   - permit 10.97.11.0/24
#   - permit 10.99.15.0/24
#   - permit 10.100.5.0/25
#   - permit 10.100.6.128/25

my_temp = Template(template, undefined=StrictUndefined)

print(my_temp.render(data))


# 2. Looping Over Dictionaries
# python처럼 for element in dict 문장을 사용하면 element의 내용물은 key 들임.
# value 접근을 위해서는 [key] notation을 이용해 접근해야함
print ("========================")
print ("Looping Over Dictionaries")
print ("========================")

data = {
    "interfaces": {
        "Ethernet1": {
         "description": "leaf01-eth51",
         "ipv4_address": "10.50.0.0/31"}
          ,
        "Ethernet2": {
         "description": "leaf02-eth51",
         "ipv4_address": "10.50.0.2/31"}
        }
}
# YAML Style
#interfaces:
#  Ethernet1:
#    description: leaf01-eth51
#    ipv4_address: 10.50.0.0/31
#  Ethernet2:
#    description: leaf02-eth51
#    ipv4_address: 10.50.0.2/31

template = """
{% for intf in interfaces -%}
{# intf는 interfaces dictionary의 key임 -#}
interface {{ intf }}
 description {{ interfaces[intf].description }}
 ip address {{ interfaces[intf].ipv4_address }}
{% endfor %}
"""

my_temp = Template(template, undefined=StrictUndefined)

print(my_temp.render(data))

# 3. items()를 활용한 dictionary access 코드 간소화
# python dict의 items()와 동일한 역할
# dict의 key, value 조합을 반환. python의 경우 tuple로 반환
print ("========================")
print ("hash + items()")
print ("========================")

template = """
{% for iname, idata in interfaces.items() -%}
interface {{ iname }}
 description {{ idata.description }}
 ip address {{ idata.ipv4_address }}
{% endfor %}
"""
my_temp = Template(template, undefined=StrictUndefined)

print(my_temp.render(data))

# 4. dictsort

data = {'my_dict': {'c':2, 'b':1, 'a':3}}
# 4.1 sort by keys
print ("========================")
print ("dictionary sort by keys")
print ("========================")

template = '''
{% for k, v in my_dict | dictsort -%}
{{ k }}, {{ v }}
{% endfor %}
'''
my_temp = Template(template, undefined=StrictUndefined)
print(my_temp.render(data))
# a, 3
# b, 1
# c, 2

# 4.2 sort by values
print ("========================")
print ("dictionary sort by value")
print ("========================")
template = '''
{% for k, v in my_dict | dictsort(by='value') -%}
{{ k }}, {{ v }}
{% endfor %}
'''

my_temp = Template(template, undefined=StrictUndefined)
print(my_temp.render(data))
# b, 1
# c, 2
# a, 3