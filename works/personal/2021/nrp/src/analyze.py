import time
import glob
import requests
from io import open, BufferedReader
import json


class BaseService:
    name: str
    def sdk(self, file: BufferedReader) -> dict: ...


def analyze(services: list[BaseService], files: list[str], wait: int = 0) -> dict[str, dict[str, dict]]:
    try:
        results = json.load(open("results.json", "r"))
    except:
        results = {}

    for file in files:
        if file in results.keys():
            continue

        print(f"analyzing {file} ({files.index(file) + 1}/{len(files)})")
        results[file] = {}
        for service in services:
            results[file][service.name] = service.sdk(open(file, "rb"))
        time.sleep(wait)
        json.dump(results, open("results.json", "w+"))
    return results
