from dataclasses import dataclass


@dataclass
class Sentiment:
    label: str
    polarity: float
