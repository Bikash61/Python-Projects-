
import random
from sty import fg  # importing foreground color

def generate_RGB():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return red, blue, green

def generate_color(red, blue, green):
    color = fg(red, blue, green)
    return color

def main():
    red, blue, green = generate_RGB()
    color = generate_color(red, blue, green)
    print(color + "I am changing the color " + fg.rs)

if __name__ == "__main__":
    main()


