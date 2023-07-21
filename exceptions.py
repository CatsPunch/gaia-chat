from fastapi.responses import JSONResponse
import logging

async def exception_handler(request, exc):
    logging.error(f"An error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content="An error occurred. Please try again later.",
    )
