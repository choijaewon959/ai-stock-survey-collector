# AI Stock Survey Collector

AI Stock Survey Collector is a daily application that leverages OpenAI's ChatGPT to gather insights and generate reports on stock market trends.

## Features

- **Automated Execution**: Runs every day to collect and process data.
- **ChatGPT Integration**: Sends requests to ChatGPT for analysis and insights.
- **Customizable Queries**: Tailor the questions sent to ChatGPT for specific stock-related topics.
- **Data Storage**: Saves responses for historical analysis and trend tracking.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-stock-survey-collector.git
    cd ai-stock-survey-collector
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables in config.json:
    - `OPENAI_API_KEY`: Your OpenAI API key.

4. Specify stocks in your interest in stocks.json:
    You can modify the `stocks.json` file to specify the stocks you want to track. The file should contain a list of stock symbols in JSON format. For example:

    ```json
    {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "NVDA": "NVIDIA Corporation",
    }
    ```

    Update this file to include the stock symbols you are interested in, and the application will use this list for its daily analysis.
    
## Usage

Run the app manually:
```bash
python src/main.py
```

Or schedule it to run daily using a cron job:
```bash
0 9 * * * /usr/bin/python3 /path/to/your/project/main.py
```
Be aware of the relative path of your config.json file when running the app.

## Configuration

Modify the `config.json` file to customize:
- Query prompts
- Scheduling preferences
- Output formats

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This app is for informational purposes only and does not provide financial advice.