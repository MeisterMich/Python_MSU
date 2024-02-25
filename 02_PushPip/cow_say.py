import cowsay as cs
import argparse as arg

parser = arg.ArgumentParser()
	
parser.add_argument("-e", "-eye_string", required=False)
parser.add_argument("-t", "-tongue", required=False)
parser.add_argument("-f", "-cowfile", required=False)
parser.add_argument("-o", "-option", required=False)
parser.add_argument("-W", "-width", required=False)
parser.add_argument("-b", "-wrap_buble", required=False)
parser.add_argument("-cf", "-custom_cowfile", required=False)
parser.add_argument("-m", "-message", required=True)
args = parser.parse_args()


def main():
    pass


if __name__=="__main__":
    main()