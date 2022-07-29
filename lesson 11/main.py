
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


def changing_of_content(input_file, output_file):
    with open('D:\pyladies\poem.txt') as input_file:
        text = input_file.read()

    text = text.replace("b", "2")

    with open("D:\pyladies\poem2.txt", "w") as output_file:
        output_file.write(text)

if __name__ == '__main__':
    print (changing_of_content(args.input_file, args.output_file))


#This program is not working and  i have an error:
    # usage: main.py[-h] input_file output_file
    # main.py: error: the following arguments are required: input_file, output_file
    #
    # the function to replace letters in file worked,
    # but when i added the argparse it didn't