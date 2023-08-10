#!/usr/bin/env python3
"""
Module to fetch and display the status from https://alu-intranet.hbtn.io/status
"""

import requests

def fetch_status():
    """
    Fetches and displays the status from https://alu-intranet.hbtn.io/status
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    fetch_status()

