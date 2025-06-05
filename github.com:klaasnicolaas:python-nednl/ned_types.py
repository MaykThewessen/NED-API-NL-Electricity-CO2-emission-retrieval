import pandas as pd
import os
import requests
import json
os.system('clear')


# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
NED_API_KEY = os.getenv("NED_API_KEY")

import asyncio

from nednl import NedNL




async def main() -> None:
    """Fetch all types from the National Energy Dashboard NL."""
    api_key: str = NED_API_KEY
    async with NedNL(api_key) as client:
        types = await client.all_types()

        for item in types:
            print(item)


if __name__ == "__main__":
    asyncio.run(main())

    