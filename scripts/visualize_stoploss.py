import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import yaml
import logging
from pathlib import Path
import random

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path='config/config.yaml'):
    """Load configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_data(data_path):
    """Load engineered data."""
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
    return df

def plot_candlestick_with_stoploss(df, output_path, window_size=30):
    """Plot candlestick chart with stop-loss levels."""
    # Select a random window of specified size
    start_idx = random.randint(0, len(df) - window_size)
    plot_df = df.iloc[start_idx:start_idx + window_size].copy()

    # Plot candlestick chart
    apds = [mpf.make_addplot(plot_df['Stoploss_Level'], color='r')]
    
    mpf.plot(plot_df, type='candle', addplot=apds, style='charles',
             title='Candlestick chart with Stop-Loss Levels', ylabel='Price',
             volume=True)
    
    # Save the plot
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    logger.info(f"Candlestick chart with stop-loss levels saved to {output_path}")

if __name__ == "__main__":
    config = load_config()
    engineered_data_path = config['data']['engineered_data_path']
    visualization_output_path = config['visualization']['output_path']
    
    # Load engineered data
    df = load_data(engineered_data_path)
    
    # Plot candlestick chart with stop-loss levels
    plot_candlestick_with_stoploss(df, visualization_output_path)
