# The MIT License (MIT)
#
# Copyright (c) 2015 Simon Marchi <simon.marchi@polymtl.ca>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import argparse
from pygdbmi import parser
from pygdbmi import visitors

def main():
    argparser = argparse.ArgumentParser(description='Pretty-print some GDB MI records')
    argparser.add_argument('input_file',
                           metavar='input-file',
                           type=str,
                           help='The file from which to read the MI data. Use - for stdin.')

    args = argparser.parse_args()
    input_file = args.input_file

    if input_file == '-':
        mi_text = sys.stdin.read()
    else:
        try:
            with open(input_file) as f:
                mi_text = f.read()
        except FileNotFoundError as e:
            sys.stderr.write(str(e) + '\n')
            sys.exit(1)

    ast = parser.parse(mi_text)
    visitor = visitors.PrettyPrintVisitor()
    visitor.visit(ast)


if __name__ == '__main__':
    main()