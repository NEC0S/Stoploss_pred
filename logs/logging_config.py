import logging
import logging.config
import yaml
import os

def setup_logging(default_path='config/logging.yaml', default_level=logging.INFO):
    """Setup logging configuration."""
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == "__main__":
    setup_logging()
