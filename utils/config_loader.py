import json

def load_config():
    with open('config/config.json', 'r') as f:
        return json.load(f)

def save_config(cfg):
    with open('config/config.json', 'w') as f:
        json.dump(cfg, f, indent=4)
