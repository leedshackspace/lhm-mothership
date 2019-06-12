from flask import Response
from json import dumps


class BadDataSupplied(Response):
    def __init__(self):
        super().__init__(
            status=400,
            response=dumps({
                "message": "No data or badly formed data was supplied."
            }),
            headers={"Content-Type": "application/json"}
        )


class NoCardIdSupplied(Response):
    def __init__(self):
        super().__init__(
            status=400,
            response=dumps({
                "message": "cardId was missing from your request."
            }),
            headers={"Content-Type": "application/json"}
        )
