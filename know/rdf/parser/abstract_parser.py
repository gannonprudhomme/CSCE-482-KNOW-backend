
from abc import ABC, abstractmethod
from enum import Enum
class EntityType(Enum):
    """ The enum that holds entity types for easy access """
    #Add more types later
    PERSON = 1
    WORK_OF_ART = 2
    BOOK = 3
    PAINTING = 4

class AbstractParser(ABC):
    """ The base class for implementing a parser for a particular source"""
    @abstractmethod
    def __init__(self, uri: str):
        """ Retrieves entity_id and rdf_uri if necessary """
        self.uri = uri

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
