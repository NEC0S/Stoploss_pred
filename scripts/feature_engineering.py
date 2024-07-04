import pandas as pd
import numpy as np
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

def load_data(data_path):
    """Load preprocessed data."""
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    return df

def calculate_volatility(df, window=14):
    """Calculate market volatility using rolling standard deviation."""
    df['Volatility'] = df['Close'].rolling(window).std()
    return df

def adjust_stoploss_based_on_volatility(df):
    """Adjust stop-loss based on market volatility."""
    df['Stoploss_Level'] = np.where(df['Volatility'] > df['Volatility'].mean(), 
                                    df['Close'] * 0.90,  # Higher volatility, larger stop-loss
                                    df['Close'] * 0.95)  # Lower volatility, smaller stop-loss
    df['Stoploss_Triggered'] = df['Low'] < df['Stoploss_Level']
    return df

def engineer_features(df):
    """Engineer features including market volatility and adjusted stop-loss."""
    df = calculate_volatility(df)
    df = adjust_stoploss_based_on_volatility(df)
    df['Daily_Return'] = df['Close'].pct_change()
    df.dropna(inplace=True)  # Drop rows with NaN values
    return df

def save_data(df, output_path):
    """Save engineered data."""
    logger.info(f"Saving engineered data to {output_path}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    config = load_config()
    cleaned_data_path = config['data']['cleaned_data_path']
    engineered_data_path = config['data']['engineered_data_path']
    
    # Load cleaned data
    df = load_data(cleaned_data_path)
    
    # Engineer features
    df = engineer_features(df)
    
    # Save engineered data
    save_data(df, engineered_data_path)
