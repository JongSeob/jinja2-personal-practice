from jinja2 import Environment, FileSystemLoader

# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))

# Load the template that uses the macro
template = env.get_template('index.html')

# Render the template
output = template.render()

# Print the rendered output
print(output)