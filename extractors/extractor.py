from abc import ABC, abstractmethod
class ExtractorInterface(ABC):
    """  An abstract base class for report extraction tools """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def extract(self, fileobject):
        raise NotImplementedError()
