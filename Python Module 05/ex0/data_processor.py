from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_store: list[str] = []
        self.rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        dato = self.data_store.pop(0)
        rank = self.rank_counter
        self.rank_counter += 1
        return (rank, dato)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is bool:
            return False
        if type(data) is int or type(data) is float:
            return True
        if type(data) is list:
            if len(data) == 0:
                return True
            for item in data:
                if type(item) is not int and type(item) is not float:
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float] |
               list[int] | list[float]) -> None:
        if self.validate(data) is False:
            raise ValueError("Improper numeric data")
        if type(data) is list:
            for item in data:
                self.data_store.append(str(item))
        else:
            self.data_store.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is bool:
            return False
        if type(data) is str:
            return True
        if type(data) is list:
            if len(data) == 0:
                return True
            for item in data:
                if type(item) is not str:
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is False:
            raise ValueError("Improper string data")
        if type(data) is list:
            for item in data:
                self.data_store.append(str(item))
        else:
            self.data_store.append(str(data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            return 'log_level' in data and 'log_message' in data
        if type(data) is list:
            if len(data) == 0:
                return True
            for item in data:
                if type(item) is not dict:
                    return False
                if 'log_level' not in item or 'log_message' not in item:
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) is False:
            raise ValueError("Improper log data")
        if type(data) is list:
            for item in data:
                entry = f"{item['log_level']}: {item['log_message']}"
                self.data_store.append(entry)
        elif type(data) is dict:
            entry = f"{data['log_level']}: {data['log_message']}"
            self.data_store.append(entry)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    num_list = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_list}")
    num_proc.ingest(num_list)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, val = num_proc.output()
        print(f" Numeric value {rank}: {val}")
    print()
    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f" Trying to validate input '42': {text_proc.validate(42)}")
    text_list = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {text_list}")
    print(" Extracting 1 value...")
    text_proc.ingest(text_list)
    rank_text, val_text = text_proc.output()
    print(f" Text value {rank_text}: {val_text}")
    print()
    print("Testing Log Processor")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_list = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {log_list}")
    print(" Extracting 2 values...")
    log_proc.ingest(log_list)
    for _ in range(2):
        rank_log, val_log = log_proc.output()
        print(f" Log entry {rank_log}: {val_log}")


if __name__ == "__main__":
    main()
