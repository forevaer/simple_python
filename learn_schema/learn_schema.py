import schema
import yaml
person_schema = schema.Schema({
    "name": str,
    "age": int,
    "gender": str
})
yml_file = "./../learn_yaml/person.yml"
with open(yml_file, "r", encoding='utf-8') as f:
    yml_content = yaml.load_all(f, yaml.FullLoader)
    for yml_data in yml_content:
        result = person_schema.validate(yml_data)

        for key, value in result.items():
            print("{_key}={_value}".format(_key=key, _value=value))
        print("*" * 10)



