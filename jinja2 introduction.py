from jinja2 import StrictUndefined, Template, Undefined


# 1. basic

# 하위 key에 접근할 때 . notation 사용
template = """hostname {{ hostname.hostname1 }}

Jinja2 Template 사이에 주석 추가 가능
{# Jinja2 Template 사이에 주석 추가 가능 -- 주석 위치에 공백 라인이 추가됨. #} 
주석 자리에 line이 추가되지 않게 하려면 닫는 괄호 앞 # 문자 앞에 - 문자 추가.
{# 주석 자리에 line이 추가되지 않게 하려면 닫는 괄호 앞 # 문자 앞에 - 문자 추가. -#}
no ip domain lookup
ip domain name local.lab
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}"""

data = {
    "hostname": {"hostname0":"core-sw-waw-01", 
                 "hostname1":"core-sw-waw-11"},
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
}

j2_template = Template(template)

print(j2_template.render(data))

# 2. key 문자열에 '.' 혹은 '-' 가 들어간 경우 . notation을 이용해 하위 dictionary에 접근 불가
#    . 대신 [] notation을 이용해 접근.
template = """
Details for 10.0.0.0/24 prefix:
  Description: {{ prefixes['10.0.0.0/24'].description }}
    Region: {{ prefixes['10.0.0.0/24'].region }}
    Site: {{ prefixes['10.0.0.0/24'].site }}
"""

data = {
  "prefixes": {
    "10.0.0.0/24": {
        "description" : "Corporate NAS", 
        "region": "Europe",
        "site": "Telehouse-West"
    }
  }
}

j2_template = Template(template)

print(j2_template.render(data))

# 3. undefined data type check
#    Default 옵션을 그대로 사용할 경우 undefined type을 만나도 에러를 발생시키지 않고 그냥 blank 처리함.
#    (추천) undefined argument를 StrictUndefined 로 설정하면 에러를 발생시킴.
template = """
name = {{ name }}
type = {{ type }}
undef type = {{ undef }}
"""

data = {"name":"me", "type":"str"}

j2_template = Template(template, undefined=Undefined) # undefined=Undefined = Default
print(j2_template.render(data))

j2_template = Template(template, undefined=StrictUndefined)
print(j2_template.render(data))

