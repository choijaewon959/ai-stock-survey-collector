import os
import json
import pandas as pd
from openai_advisor import OpenAIAdvisor

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

def main():
    """
    Main function to load API key and execute the logic.
    """
    try:
        api_key = load_api_key()
        ai_advisor = OpenAIAdvisor(api_key)
        advices = ai_advisor.get_advice()
        df = pd.DataFrame(advices)
        df.to_csv("../advice.csv", index=False)
        print("Advice saved to advice.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()