def __init__(self):
        self.product = None

        def get_valid_input(self, prompt):
         while True:
            try:
                return input(prompt)
            except ValueError:
                print("Invalid input. Please try again.")

        def display_header(self):
          print("Month\tStock Level\tUnits Sold")
          class Product:
            def __init__(self, code: str, name: str, sale_price: float, export_price: float, stock: int, m_units: int):
               self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = export_price
        self.stock_level = stock
        self.estimated_monthly_units = m_units
        self.total_units_sold = 0
        self.total_units_manufactured = 0
    
        def process_monthly_units(self):
          units_sold = max(0, min(self.stock_level, self.estimated_monthly_units + random.randint(-10, 10)))
        self.total_units_sold += units_sold
        self.total_units_manufactured += self.estimated_monthly_units
        self.stock_level += self.estimated_monthly_units - units_sold
    
        def calculate_net_profit(self):
         revenue = self.total_units_sold * self.sale_price
        costs = self.total_units_manufactured * self.manufacture_cost
        net_profit = revenue - costs
        return net_profit

        def generate_statement(self):
         statement = ""
        statement += f"Product Name: {self.name}\n"
        statement += f"Sale Price: {self.sale_price}\n"
        statement += f"Manufacture Cost: {self.manufacture_cost}\n"
        statement += f"Initial Stock: {self.stock_level}\n"
        return statement
    class Application:
         def __init__(self):
        self.product = None

     def get_valid_input(self, prompt, Amro x: self.unsubscribe):
