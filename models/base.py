import uuid
from datetime import datetime, timezone


class Base:
    """Base class for all models"""
    
    __counter = 0

    def __init__(self, id: str = None, 
                 created_at: str = None, updated_at: str = None) -> None:
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

        if created_at is None:
            self.__created_at = datetime.now(tz=timezone.utc)
        else:
            try:
                self.__created_at = datetime.strptime(
                    created_at, "%d %B %Y : %H:%M:%S")
            except:
                raise ValueError(
                    f'{created_at} must be in the format: %d %B %Y : %H:%M:%S, day month year : hour:minute:second. Month must be in full.')

        if updated_at is None:
            self.__updated_at = datetime.now(tz=timezone.utc)
        else:
            try:
                self.__updated_at = datetime.strptime(
                    updated_at, "%d %B %Y : %H:%M:%S")
            except:
                raise ValueError(
                    f'{updated_at} must be in the format: %d %B %Y : %H:%M:%S, day month year : hour:minute:second. Month must be in full.')

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

    @updated_at.setter
    def updated_at(self, updated_at: datetime) -> None:
        """Setter for the updated_at attribute

        Args:
            updated_at (str): The updated_at to set
        """
        self.__updated_at = updated_at
