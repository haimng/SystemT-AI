import sys
import os
from utils.db import get_stock_prices

def load_data():
  """Load all btcusd prices from the database."""
  data = get_stock_prices(filters={'symbol': 'btcusd'}, order="date ASC", limit=None)
  return data

# python -m updown_models.model_pipeline
if __name__ == "__main__":
  data = load_data()
  print(data)