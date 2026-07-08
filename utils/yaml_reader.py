from pathlib import Path
import yaml


def read_yaml(file_path):
    file_path = Path(file_path)

    with file_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data