import argparse

def getArgument():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f'desc',
        epilog='epilog'
    )

    parser.add_argument("-v", "--verbose", action="count", default=0, help="verbose 1, 2")

    return parser.parse_args()