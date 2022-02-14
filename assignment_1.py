# PART A
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = '[A-Z][a-z]*'
    get_names = re.findall(pattern, simple_string)
    return(get_names)


# PART B
import re
def grades():
    with open ("C:/Users/001149745/OneDrive - LOJAS RENNER SA/Documentos/Gabrielle_N/~CURSOS/curso_2/grades.txt") as file:
        grades = file.read()

    # YOUR CODE HERE
    pattern = '\w[\w ]*: B'
    get_list = re.findall(pattern, grades)
    return (get_list)


# PART C
import re
def logs():
    with open("C:/Users/001149745/OneDrive - LOJAS RENNER SA/Documentos/Gabrielle_N/~CURSOS/curso_2/logdata.txt") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
    pattern = []
    
    pattern_host = re.findall('(.*?)\-', logdata)
    pattern_user = re.findall('\-(.*?)\[', logdata)
    pattern_time = re.findall('\[(.*?)\]', logdata)
    pattern_request = re.findall('\"(.*?)\"]', logdata)

    pattern.append({'host':pattern_host, 'user_name':pattern_user,
                    'time':pattern_time, 'request':pattern_request})
    return(pattern)
