class restaurantClass:
    def __init__(self, name: str) -> None:
        # Typechecking here is not really needed.
        self.name: str = name
        self.totalServed: int = 0 # lifetime serves
        self.served: int = 0 # daily serves
        self.orders: list = []

    def close(self):
        print(f"{self.name} is closing for the day! \n")
        self.served = 0
        self.orders.clear()

    def track(self, order: dict):
        for item in order.values():
            self.orders.append(item)