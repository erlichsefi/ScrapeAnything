def to_text_file(text,filename):
    import datetime
    
    with open(filename, 'a') as file:
        file.write("\nExecution Time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "\n")
        file.write('-----\n')
        file.write(text)
        