from typing import List
import json

class Database:
    def __init__(self, storage_strategy: str = "json"):
        self.storage_strategy = storage_strategy

    def store_data(self, data: List[dict]):
        # Store scraped data based on the storage strategy
        if self.storage_strategy == "json":
            with open("scraped_data.json", "w") as f:
                json.dump(data, f, indent=4)
        # Add other storage strategies as needed

