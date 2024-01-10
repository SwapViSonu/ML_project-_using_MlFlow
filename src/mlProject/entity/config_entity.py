from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    query: str
