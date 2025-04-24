import sys
import json
from pathlib import Path

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main()
