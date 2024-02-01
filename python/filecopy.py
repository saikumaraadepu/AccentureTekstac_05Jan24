with open('file_in.txt','r')as input_file:
    with open('file_out.txt','w')as output_file:
        for line in input_file:
            output_file.write(line)

with open('file_out.txt','r')as output_file:
    print(output_file.read())