# Python argparse: unrecognized arguments error

import argparse


parser = argparse.ArgumentParser(
    description='A sample Argument Parser.'
)

parser.add_argument('filename')

parser.add_argument('-c', '--count')

parser.add_argument('-v', '--verbose', action='store_true')

# ✅ removed sys.argv
args = parser.parse_args()

print(f'args.filename {args.filename}')

print(f'args.count {args.count}')

print(f'args.verbose {args.verbose}')