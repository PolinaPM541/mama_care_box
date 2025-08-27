from fastapi import status

responses = {
    status.HTTP_200_OK: {
        "description": " successfully created",
    },
    status.HTTP_404_NOT_FOUND: {
        "description": " not found ",
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": " internal server error",
    },
}
