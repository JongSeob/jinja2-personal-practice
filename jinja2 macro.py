from jinja2 import Template

template = '''
{% macro test (arg) %}
macro test. arg = {{ arg }}
{{ caller() }}
{% endmacro %}

{% call test(123) %}
inside call block
{% endcall %}
'''

template2 = '''
{% macro test (arg) %}
macro test. arg = {{ arg }}
{%- endmacro %}

{{ test(123) }}
inside call block
'''

tmpl = Template(template, trim_blocks=True, lstrip_blocks=True)
print(tmpl.render())

tmpl = Template(template2, trim_blocks=True, lstrip_blocks=True)
print(tmpl.render())