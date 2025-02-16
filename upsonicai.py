from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

price_taker_agent = Agent("Supermarket Price Tracker", model="azure/gpt-4o")

class Price(ObjectResponse):
    market:str
    best_price:float
    link:str


market1= "Walmart"
market2= "Kroger"
product= "Coca-Cola Classic Soda Pop, 12 fl oz Cans, 24 Pack"

price_task = Task(
    "Search for the product in the markets and find",
    tools=[BrowserUse],
    response_format=Price,
    context=[market2, market1, product]
)
price_taker_agent.print_do(price_task)


  