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

def clean_data(raw_data_path):
    """Clean and prepare raw data."""
    logger.info(f"Loading raw data from {raw_data_path}")
    df = pd.read_csv(raw_data_path)
    
    # Perform any cleaning or transformation
    # Example: Drop unnecessary columns
    df_cleaned = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].copy()
    
    return df_cleaned

def save_clean_data(df_cleaned, output_path):
    """Save cleaned data to a file."""
    logger.info(f"Saving cleaned data to {output_path}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df_cleaned.to_csv(output_path, index=False)

if __name__ == "__main__":
    config = load_config()
    raw_data_path = config['data']['raw_data_path']
    cleaned_data_path = config['data']['cleaned_data_path']
    
    # Clean raw data
    df_cleaned = clean_data(raw_data_path)
    
    # Save cleaned data
    save_clean_data(df_cleaned, cleaned_data_path)
