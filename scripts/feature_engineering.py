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

def engineer_features(df):
    """Engineer new features based on existing data."""
    logger.info("Engineering features")
    
    # Example feature engineering
    # Add your custom feature engineering logic here
    # For example, calculating moving averages, daily returns, etc.
    df['Daily_Return'] = df['Close'].pct_change() * 100  # Example: Daily returns as percentage
    
    return df

def save_data(df, output_path):
    """Save the engineered data to a file."""
    logger.info(f"Saving engineered data to {output_path}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    config = load_config()
    cleaned_data_path = config['data']['cleaned_data_path']
    feature_data_path = config['data']['feature_data_path']
    
    # Load cleaned data
    logger.info(f"Loading data from {cleaned_data_path}")
    df = pd.read_csv(cleaned_data_path)
    
    # Engineer features
    df = engineer_features(df)
    
    # Save engineered data
    save_data(df, feature_data_path)
