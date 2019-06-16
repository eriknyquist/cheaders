import argparse
from cheaders import Generator

parser = argparse.ArgumentParser(description="C header file generator")
parser.prog = "cheaders"

parser.add_argument('input_file', type=str,
    help="C source file to generate a header file for")
parser.add_argument('-d', '--doxygen-comments', action='store_true',
    dest='doxygen_comments', help="Print version information")
parser.add_argument('-a', '--author', dest='author', type=str,
    help="author name", default=None)

args = parser.parse_args()

h = Generator(args.input_file, author=args.author)

print(h.generate(doxygen_comments=args.doxygen_comments))

