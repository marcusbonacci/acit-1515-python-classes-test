from classes.customer import customerClass
from classes.restaurant import restaurantClass

# After comparing Python to LUA I'm starting to understand some of the differences.

# There are many ways I can take this project
#   - proper class -> class interactions and cleanup
#       - the creation of customers, tracking of orders, etc, should be handled inside of the correct classes, in order to cleanup main.py
#   - Might consider implementing the observer pattern to handle events...
#       ? scheduler
#       ? ticks
#       ? eventConnection
#       * solve via doubly linked list or regular list... explore both options
#           - https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
#           - https://www.geeksforgeeks.org/doubly-linked-list/

# TODO: 
#   - Add most common sideCourse, secondCourse, thirdCourse
#   - Use proper paradigms and methods  
#   - Cleanup the code
#   - Incorporate Pep8 style standard

def main():
    restaurant = restaurantClass("John's restaurant")

    print(f"Opening {restaurant.name} \n")

    # Create 30 customers
    for _ in range(0, 30):
        customer = customerClass()
        order = customer.orderFood()

        restaurant.track(order)
        restaurant.served += 1
        restaurant.totalServed += 1

        del(customer)

    print(f"Served: {restaurant.served}")
    print(f"Lifetime Served: {restaurant.totalServed}")
    print(f"First order: {restaurant.orders[0]}")
    print(f"Last order: {restaurant.orders[-1]}")

    restaurant.close()

if __name__ == "__main__":
    main()