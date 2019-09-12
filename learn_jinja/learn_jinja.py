from jinja2 import Template

source = '''
    hello, my name is {{ own }} , and you, what's your name? 
    find, my name is {{ other }}, nice to meet you!
'''
template = Template(source)
result = template.render(own="godme", other="judas")
print(result)