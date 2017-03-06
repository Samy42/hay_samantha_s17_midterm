import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--city", dest="City",help="enter a string value",
                    type=str)
parser.add_argument("--number", dest="Number",help="enter a number value",
                    type=int)

args = parser.parse_args()
print(args.City)
print(args.Number)
