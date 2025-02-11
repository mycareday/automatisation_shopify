import random
import requests

def secure_connection():
    proxies = ["proxy1", "proxy2", "proxy3"]
    selected_proxy = random.choice(proxies)
    print(f"Using proxy: {selected_proxy}")
    requests.get("http://example.com", proxies={"http": selected_proxy})
