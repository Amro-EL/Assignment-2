import random

class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_production):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_production = estimated_production

    def simulate_monthly_stock(self):
        monthly_stock = []
        total_units_sold = 0

        for month in range(1, 13):
            units_sold = random.randint(self.estimated_production - 10, self.estimated_production + 10)
            self.stock_level += self.estimated_production
            self.stock_level -= units_sold
            total_units_sold += units_sold
            monthly_stock.append((month, self.stock_level, units_sold))

        return monthly_stock, total_units_sold

class PredictedStockStatement:
    def __init__(self, product, monthly_stock, total_units_sold):
        self.product = product
        self.monthly_stock = monthly_stock
        self.total_units_sold = total_units_sold

    def calculate_net_profit(self):
        total_manufactured = self.product.estimated_production * 12
        revenue = self.total_units_sold * self.product.sale_price
        costs = total_manufactured * self.product.manufacture_cost
        return revenue - costs

    def generate_statement(self):
        print("\nPredicted Stock Statement")
        print("Product Code:", self.product.product_code)
        print("Product Name:", self.product.product_name)
        print("Sale Price:", self.product.sale_price)
        print("Manufacture Cost:", self.product.manufacture_cost)
        print("Initial Stock Level:", self.product.stock_level)
        print("Estimated Monthly Production:", self.product.estimated_production)
        
        print("\nMonthly Stock Details:")
        print("Month\tStock Level\tUnits Sold")
        for month, stock, units_sold in self.monthly_stock:
            print(f"{month}\t{stock}\t\t{units_sold}")
        
        net_profit = self.calculate_net_profit()
        print("\nNet Profit/Loss:", net_profit)

class Application:
    def get_user_input(self, prompt, validation_func):
        while True:
            try:
                value = validation_func(input(prompt))
                return value
            except ValueError as x:
                print(x)

    def main(self):
        print("WELCOME to Product Stock Simulator")
        
        product_code = self.get_user_input(
            "Enter your Product Code(100-1000): ",
            lambda x: int(x) if 100 <= int(x) <= 1000 else (_ for _ in ()).throw(ValueError("Invalid Product Code."))
        )

        product_name = input("Product Name: ")
        
        sale_price = self.get_user_input(
            "Enter your Sale Price(greater than 0): ",
            lambda x: float(x) if float(x) > 0 else (_ for _ in ()).throw(ValueError("Invalid Sale Price."))
        )
        
        manufacture_cost = self.get_user_input(
            "Enter your Manufacture Cost(greater than 0): ",
            lambda x: float(x) if float(x) > 0 else (_ for _ in ()).throw(ValueError("Invalid Manufacture Cost."))
        )
        
        stock_level = self.get_user_input(
            "Enter your Initial Stock Level(greater than 0): ",
            lambda x: int(x) if int(x) > 0 else (_ for _ in ()).throw(ValueError("Invalid Stock Level."))
        )
        
        estimated_production = self.get_user_input(
            "Enter your estimated month Production which is greater or equals to 0: ",
            lambda x: int(x) if int(x) >= 0 else (_ for _ in ()).throw(ValueError("Invalid Production Value."))
        )

        product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_production)
        monthly_stock, total_units_sold = product.simulate_monthly_stock()
        statement = PredictedStockStatement(product, monthly_stock, total_units_sold)
        statement.generate_statement()

if __name__ == "__main__":
    app = Application()
    app.main()