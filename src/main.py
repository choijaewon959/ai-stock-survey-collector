import os
import json
import pandas as pd
from openai_advisor import OpenAIAdvisor
from datetime import datetime

def load_api_key(config_path="config.json"):
    """
    Load API key from a configuration file.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    api_key = config.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found in the configuration file.")
    
    return api_key

def load_stock_list(stock_list_path="stocks.json"):
    """
    Load stock list from a JSON file.
    """
    if not os.path.exists(stock_list_path):
        raise FileNotFoundError(f"Stock list file '{stock_list_path}' not found.")
    
    with open(stock_list_path, 'r') as file:
        stock_list = json.load(file)

    if isinstance(stock_list, dict):
        stock_list = list(stock_list.values())

    return stock_list

def main():
    """
    Main function to load API key and execute the logic.
    """
    try:
        # parse config files
        api_key = load_api_key()
        ai_advisor = OpenAIAdvisor(api_key)
        stock_list = load_stock_list()
        print("Available stocks:", stock_list)

        for s in stock_list:
            print(f"Getting advice for {s}...")
            advices = ai_advisor.get_advice(s)
            df = pd.DataFrame(advices)

            # Save the advice to a CSV file
            print(f"Saving advice for {s} to CSV...")
            if not os.path.exists('output'):
                os.makedirs('output')
            current_date = datetime.now().strftime("%Y-%m-%d")
            filename = f'''output/output_{s}_{current_date}.csv'''
            filepath = os.path.join(os.getcwd(), filename)
            df.to_csv(filepath, index=False)
            print(f"Advice for {s} saved to output directory.\n")

        print("All tasks completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()