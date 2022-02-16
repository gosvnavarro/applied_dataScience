# PART A
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = '[A-Z][a-z]*'
    get_names = re.findall(pattern, simple_string)
    return(get_names)

names()

# PART B
import re
def grades():
    with open ("C:/Users/001149745/OneDrive - LOJAS RENNER SA/Documentos/Gabrielle_N/~CURSOS/curso_2/grades.txt") as file:
        grades = file.read()

    # YOUR CODE HERE
    pattern = '(.*): B'
    #pattern = '([A-Z][a-z]+ [A-Z][a-z]+): B' <- TESTAR
    #pattern = '[\w]*\ [\w]*(?=:\ B)' <- TESTAR
    get_list = re.findall(pattern, grades)
    return (get_list)

grades()

# PART C
import re
def logs():
    with open("C:/Users/001149745/OneDrive - LOJAS RENNER SA/Documentos/Gabrielle_N/~CURSOS/curso_2/logdata.txt") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
        list_dict = []
    
    pattern="""(?P<host>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)
                    (\ - \ )
                    (?P<user_name>(\w*)(\S))
                    (\  \S)
                    (?P<time>\d+\S\w*\S\d+\S\d+\S\d+\S\d+\s\S\d+)
                    (\S\s\S)
                    (?P<request>\w*\s\S*\s\w*\S\d.\d*)
                 """
    for item in re.finditer(pattern,logdata,re.VERBOSE): 
        list_dict.append(item.groupdict())
    return list_dict

logs()
