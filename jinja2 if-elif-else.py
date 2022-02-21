from jinja2 import StrictUndefined, Template, Undefined

# 1. if else
print("========================")
print("if else")
print("========================")

template = """
hostname {{ hostname }}
{% if eos_ver >= 4.22 -%}
Detected EOS ver {{ eos_ver }}, using new command syntax.
{% else -%}
Detected EOS ver {{ eos_ver }}, using old command syntax.
{% endif %}
"""

data = {
    "eos_ver": 4.22,
    "hostname": "arista_new_eos"
}

my_temp = Template(template, undefined=StrictUndefined)
print(my_temp.render(data))

data["eos_ver"] = 4.19
print(my_temp.render(data))

# 2. if elf else
print("========================")
print("if elf else")
print("========================")

template = '''hostname {{ hostname }}
ip routing

{% for intf, idata in interfaces.items() -%}
interface {{ intf }}
  ip address {{ idata.ip }}/{{ idata.mask }}
{%- endfor %}

{% if routing_protocol == 'bgp' -%}
router bgp {{ bgp.as }}
  router-id {{ interfaces.Loopback0.ip }}
  network {{ interfaces.Loopback0.ip }}/{{ interfaces.Loopback0.mask }}
{%- elif routing_protocol == 'ospf' -%}
router ospf {{ ospf.pid }}
  router-id {{ interfaces.Loopback0.ip }}
  network {{ interfaces.Loopback0.ip }}/{{ interfaces.Loopback0.mask }} area 0
{%- else -%}
  ip route 0.0.0.0/0 {{ default_nh }}
{%- endif %}'''

my_temp = Template(template, undefined=StrictUndefined)

print('======= Device running BGP: =======')
data = {
  "bgp": {
    "as": 65001
  }, 
  "interfaces": {
    "Loopback0": {
      "ip": "10.0.0.1", 
      "mask": 32
    }
  }, 
  "hostname": "router-w-bgp", 
  "routing_protocol": "bgp"
}
print(my_temp.render(data))

print('======= Device running OSPF: =======')
data = {
  "interfaces": {
    "Loopback0": {
      "ip": "10.0.0.2", 
      "mask": 32
    }
  }, 
  "hostname": "router-w-ospf", 
  "ospf": {
    "pid": 1
  }, 
  "routing_protocol": "ospf"
}
print(my_temp.render(data))

print('======= Device with default route only: =======')
data = {
  "interfaces": {
    "Ethernet1": {
      "ip": "10.10.0.10", 
      "mask": 24
    }
  }, 
  "hostname": "router-w-defgw", 
  "default_nh": "10.10.0.1",
  "routing_protocol": ""
}
print(my_temp.render(data))
