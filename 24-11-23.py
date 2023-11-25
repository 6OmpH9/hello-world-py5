import cairo, PIL, argparse, math, random
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("--width", default=3000, type=int)
    parser.add_argument("--height", default=2000, type=int)
    parser.add_argument("-o", "--orbit" action="store_true")
    parser.add_argument("-l", "--line", action="store_true")
    parser.add_argument("-s",  "--sunsize", default=random.randint(200, 400), type=int)
    parser.add_argument("-bs", "--bordersize", default=50, type=int )
    parser.add_argument("-n", "--noise", default=.4, type=float)
    args = parser.parse_args()

    
