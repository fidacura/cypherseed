# cypherseed/cypherseed/__init__.py

# import necessary modules for external use
from .generator import generate_passphrase
from .wordlists import load_wordlist
from .password_strength import calculate_strength

# import main function from root-level cypherseed.py
import os
import sys

# add the project root to the python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# import the main function from the root-level script
import importlib.util
spec = importlib.util.spec_from_file_location("cypherseed_module", 
                                             os.path.join(os.path.dirname(os.path.dirname(__file__)), "cypherseed.py"))
cypherseed_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cypherseed_module)
main = cypherseed_module.main

# define what symbols to export when using 'from cypherseed import *'
__all__ = ['generate_passphrase', 'load_wordlist', 'calculate_strength', 'main']