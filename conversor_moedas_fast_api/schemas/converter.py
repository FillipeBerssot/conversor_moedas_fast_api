from typing import List

from pydantic import BaseModel


class ConverterOutputSchema(BaseModel):
    message: str
    data: List[dict]
