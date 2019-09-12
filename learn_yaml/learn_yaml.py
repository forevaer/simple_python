import yaml


source_file = open("person.yml", 'r', encoding='utf-8')
yml_content = yaml.load_all(source_file, yaml.FullLoader)
for person in yml_content:
    print(person)