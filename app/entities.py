from dataclasses import dataclass

@dataclass
class Task:
    header: str
    body: str
    done: bool
    