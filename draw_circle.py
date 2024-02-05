# draw a circle of squares using Turtle
import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def draw_circle_of_squares(num_squares, side_length):
    for _ in range(num_squares):
        draw_square(side_length)
        turtle.forward(side_length)
        turtle.left(360 / num_squares)

def main():
    turtle.speed(2)
    turtle.bgcolor("white")
    turtle.color("blue")

    num_squares = 36  # You can adjust the number of squares
    side_length = 30

    draw_circle_of_squares(num_squares, side_length)

    turtle.hideturtle()  # Hide the turtle cursor
    turtle.done()

if __name__ == "__main__":
    main()
