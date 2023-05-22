# Execution Command

```bash
%> python jinja2.py
```

# Description

***index.html*** template imports "macro greet()" from ***macros.html***,
and call this macro inside template.

**FileSystemLoader** is necessary to permit a template to import other templates.
The path './' inserted in the constructor of FileSystemLoader is equal to the location of target template file ("index.html").
And relative path is used in index.html for the access to other files.

# The point that not treated in this example

{% call %} ~ {% endcall %} and {{ caller }} are not used in this example.
But if call & caller are used in templates, "**with context**" is appeded behind.

```html
{% import "./macros/macros.html" as macros with context %}
```
