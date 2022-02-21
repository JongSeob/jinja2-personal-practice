from jinja2 import StrictUndefined, Template, Undefined

# 1. 조건이 참인 경우에만 loop 진행
print('1. ---------------------------------------------------')

template = '''
{#- ipv4_address attribute가 존재하는 경우에만 rendering을 진행한다. -#}
{% for intf, idata in interfaces.items() if idata.ipv4_address is defined -%}
{{ intf }} - {{ idata.description }}: {{ idata.ipv4_address }}
{% endfor %}
'''

data = {
    "interfaces": {
        "Loopback0": {
            "description": "Management plane traffic",
            "ipv4_address": "10.255.255.34/32"
        },
        "Management1": {
            "description": "Management interface",
            "ipv4_address": "10.10.0.5/24"
        },
        "Ethernet1": {
            "description": "Span port - SPAN1"
        },
        "Ethernet2": {
            "description": "PortChannel50 - port 1"
        },
        "Ethernet51": {
            "description": "leaf01-eth51",
            "ipv4_address": "10.50.0.0/31"
        },
        "Ethernet52": {
            "description": "leaf02-eth51",
            "ipv4_address": "10.50.0.2/31"
        }
    }
}

my_temp = Template(template, undefined=StrictUndefined)
print(my_temp.render(data))

# 2. in : 리스트, 해시에 특정 value가 존재하는지 확인
print('2. ---------------------------------------------------')

template = '''{% if 'Loopback0' in interfaces -%}
sflow source-interface Loopback0
snmp-server source-interface Loopback0
ip radius source-interface Loopback0
{%- else %}
sflow source-interface Management1
snmp-server source-interface Management1
ip radius source-interface Management1
{% endif %}
'''

my_temp = Template(template, undefined=StrictUndefined)
print(my_temp.render(data))
