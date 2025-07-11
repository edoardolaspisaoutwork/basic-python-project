""" Basic response class for API responses """
from pydantic import BaseModel

class BasicResponse:
    """ Basic response class for API responses """
    data: BaseModel | None = None
    status: int = 200
    error: str | None = None

    def __init__(self, data: str | None = None, status: int = 200, error: str | None = None) -> None:
        """ Basic response class for API responses """
        self.data = data
        self.status = status
        self.error = error

