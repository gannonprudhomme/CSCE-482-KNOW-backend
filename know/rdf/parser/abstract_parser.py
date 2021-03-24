from abc import ABC, abstractmethod

class AbstractParser(ABC):
    """ The base class for implementing a parser for a particular source"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def parse(self) -> dict:
        """Calls other parse functions depending on the entity type"""

    @abstractmethod
    def get_entity_type(self) -> str:
        """ Retrieves the entity type."""

    @abstractmethod
    def parse_person(self) -> dict:
        """ Parse a person """

    @abstractmethod
    def parse_work_of_art(self) -> dict:
        """ Parse a work of art """
