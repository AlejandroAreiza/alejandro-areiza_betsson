from config.utils import Path, Type, TypeVar, json

T = TypeVar("T")


class DataProvider:
    @staticmethod
    def get_data(file_path: str, dto_class: Type[T]) -> T:
        try:
            if not file_path:
                raise ValueError("file_path cannot be null or empty")

            path = Path(file_path)

            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")

            if not path.is_file():
                raise ValueError(f"Path is not a file: {file_path}")

            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return dto_class(**data)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file {file_path}: {str(e)}")
        except TypeError as e:
            raise ValueError(f"Failed to map JSON to {dto_class.__name__}: {str(e)}")
