with open('name.txt') as f:
    my_name = f.read()

with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' +  my_name)
