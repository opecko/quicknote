from dataclasses import asdict, dataclass


@dataclass
class Note:
    text: str
    done: bool = False

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Note(**data)
