import yfinance as yf
import pandas as pd
import yaml
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path='config/config.yaml'):
    """Load configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def download_data(ticker, start_date, end_date):
    """Download historical market data from Yahoo Finance."""
    logger.info(f"Downloading data for {ticker} from {start_date} to {end_date}")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def save_data(df, output_path):
    """Save the downloaded data to a file."""
    logger.info(f"Saving data to {output_path}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path)

if __name__ == "__main__":
    config = load_config()
    raw_data_path = config['data']['raw_data_path']
    
    # Customize the parameters as needed
    ticker = "AAPL"  # Example: Apple Inc.
    start_date = "2015-01-01"
    end_date = "2023-01-01"
    
    df = download_data(ticker, start_date, end_date)
    save_data(df, raw_data_path)
