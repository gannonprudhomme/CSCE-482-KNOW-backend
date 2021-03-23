from abc import ABC, abstractmethod

class AbstractParser(ABC):
    """ The base class for implementing a parser for a particular source"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def parse(self) -> dict:
        """Calls other parse functions depending on the entity type"""
        pass

    @abstractmethod
    def get_entity_type(self) -> str:
        """ Retrieves the entity type."""
        pass

    @abstractmethod
    def parse_person(self) -> dict:
        pass

    @abstractmethod
    def parse_work_of_art(self) -> dict:
        pass
