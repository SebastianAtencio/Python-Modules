import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_store: list[str] = []
        self.rank_counter: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        dato = self.data_store.pop(0)
        rank = self.rank_counter
        self.rank_counter += 1
        return (rank, dato)


class DataStream():
    def __init__(self) -> None:
        self.processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            worked = False
            for proc in self.processor:
                if proc.validate(item):
                    proc.ingest(item)
                    worked = True
                    break
            if not worked:
                print(f"DataStream error - Can't process element"
                      f"in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processor:
            print("No processor found, no data")
            return
        for proc in self.processor:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc.rank_counter + len(proc.data_store)
            remaining = len(proc.data_store)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) is False:
            raise ValueError("Improper numeric data")
        if type(data) is list:
            for item in data:
                self.data_store.append(str(item))
        else:
            self.data_store.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
    def validate(self, data: typing.Any) -> bool:
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
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    tool = DataStream()
    num = NumericProcessor()
    tool.print_processors_stats()
    tool.register_processor(num)
    print()
    print("Registering Numeric Processor")
    print()
    data = [
            'Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42, ['Hi', 'five']
            ]
    print(f"Send first batch of data on stream: {data}")
    tool.process_stream(data)
    tool.print_processors_stats()
    text = TextProcessor()
    logproc = LogProcessor()
    tool.register_processor(text)
    tool.register_processor(logproc)
    print()
    print("Registering other data processors")
    print("Send the same batch again")
    tool.process_stream(data)
    tool.print_processors_stats()
    print()
    print("Consume some elements from the data processors:"
          "Numeric 3,Text 2, Log 1")
    for _ in range(3):
        num.output()
    for _ in range(2):
        text.output()
    logproc.output
    tool.print_processors_stats()


if __name__ == "__main__":
    main()
