from dataclasses import dataclass

from src.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CodeException(ServiceException):
    @property
    def message(self):
        return 'Auth code exception occurred'


@dataclass(eq=False)
class CodeNotFoundException(CodeException):

    @property
    def message(self):
        return 'Code not found'


@dataclass(eq=False)
class CodesNotEqualException(CodeException):

    @property
    def message(self):
        return 'Codes are not equal'
