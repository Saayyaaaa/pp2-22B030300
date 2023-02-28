def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

my_string = "my_snake_case_string"
new_string = snake_to_camel(my_string)
print(new_string)
