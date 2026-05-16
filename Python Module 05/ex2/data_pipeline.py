from typing import Any, Protocol
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream():
    def __init__(self) -> None:
        self.processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processor:
            extra_data = []
            count = 0
            while count < nb and len(proc.data_store) > 0:
                tupla = proc.output()
                extra_data.append(tupla)
                count += 1
            if extra_data:
                plugin.process_output(extra_data)


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

    def ingest(self, data: int | float | list[int | float]) -> None:
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


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for rank, val in data:
            values.append(val)
        print("CSV Output:")
        print(",".join(values))


class JsonPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_string = "{"
        for i in range(len(data)):
            rank, valor = data[i]
            pieza = f'"item_{rank}": "{valor}"'
            json_string += pieza
            if i < len(data) - 1:
                json_string += ", "
        json_string += "}"
        print("JSON Output:")
        print(json_string)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    tool = DataStream()
    tool.print_processors_stats()
    print()
    print("Registering Processors")
    num = NumericProcessor()
    text = TextProcessor()
    logproc = LogProcessor()
    tool.register_processor(num)
    tool.register_processor(text)
    tool.register_processor(logproc)
    print()
    data = [
            'Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42, ['Hi', 'five']
            ]
    print()
    print(f"Send first batch of data on stream: {data}")
    tool.process_stream(data)
    print()
    tool.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin")
    tool.output_pipeline(3, CSVPlugin())
    print()
    tool.print_processors_stats()
    print()
    data2 = [
             21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
             [{'log_level': 'ERROR', 'log_message': '500 server crash'},
              {'log_level': 'NOTICE', 'log_message': 'Certificate '
              'expires in 10 days'}],
             [32, 42, 64, 84, 128, 168], 'World hello'
            ]
    print(f"Send another batch of data: {data2}")
    tool.process_stream(data2)
    print()
    tool.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin")
    tool.output_pipeline(5, JsonPlugin())
    print()
    tool.print_processors_stats()


if __name__ == "__main__":
    main()
