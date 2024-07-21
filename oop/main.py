from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create instances of Rectangle and Circle
    rect = Rectangle(5, 3)
    circ = Circle(2)

    # Print the areas of the shapes
    print(f"The area of the rectangle is: {rect.area()}")
    print(f"The area of the circle is: {circ.area()}")

if __name__ == "__main__":
    main()