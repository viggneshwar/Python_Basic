class CostingClass:

    def __init__(self, cost_per_hour):#Instantiate this class with parameter of cost_per_hour
        self.cost_per_hour = cost_per_hour

    def calculate_installtime(self, product):
        """
        Returns installation time based on product type.
        """
        product = product.lower().strip()

        install_times = {
            "voip": 5,
            "stb": 3,
            "router": 2,
            "switch": 4  }
        hours_for_installation=install_times.get(product, 10)
        return hours_for_installation

    def calculate_cost(self, hours_for_installation):
        final_cost = self.cost_per_hour * hours_for_installation
        return final_cost



