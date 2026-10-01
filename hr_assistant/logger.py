"""Simple logger configuration for the HR Assistant."""

import logging

def get_logger(name: str):
    """Return a configured logger instance."""
    logger = logging.getLogger(name)
    
    # Prevent adding duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler with formatting
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger
