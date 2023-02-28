import re
def camel_to_snake(camel_str):
    snake_str = re.sub('([A-Z])', '_\\1', camel_str).lower()
    if snake_str[0] == '_':
        snake_str = snake_str[1:]
    return snake_str

my_string = "ConvertGivenCamelCaseStringToSnakeCase"
new_string = camel_to_snake(my_string)
print(new_string)
