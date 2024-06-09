import uuid
from datetime import datetime, timezone


class Base:
    """Base class for all models"""

    def __init__(self, id=None) -> None:
        """Base class constructor

        Args:
            id (str): The id of the object

        Raises:
            ValueError: If the id is not a valid UUID

        Returns:
            None
        """
        if id is None:
            self.__id = str(uuid.uuid4())
        else:
            try:
                uuid.UUID(id)
            except ValueError as e:
                raise ValueError("Invalid id")
            
            self.__id = id

        self.__created_at = datetime.now(tz=timezone.utc)
        self.__updated_at = None

    @property
    def id(self) -> str:
        """Getter for the id attribute"""
        return self.__id

    @property
    def created_at(self) -> datetime:
        """Getter for the created_at attribute"""
        return self.__created_at

    @property
    def updated_at(self) -> datetime:
        """Getter for the updated_at attribute"""
        return self.__updated_at
