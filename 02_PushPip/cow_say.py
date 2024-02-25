import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", default="cow", required=False)
parser.add_argument("-o", default="-b", required=False)
parser.add_argument("-e", default="oo", required=False)
parser.add_argument("-t", default="U", required=False)
parser.add_argument("-W", default=40, required=False)
parser.add_argument("-b", default=True, required=False)
parser.add_argument("-cf", required=False)
parser.add_argument("-m", required=True)
args = parser.parse_args()

def main():
    print(cowsay.cowsay(message=args.m,
                        eyes=args.e,
                        tongue=args.t,
                        width=args.W,
                        wrap_text=args.b))

if __name__ == '__main__':
    main()