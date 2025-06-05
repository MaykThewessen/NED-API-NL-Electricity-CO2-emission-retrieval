import pandas as pd
import os
import asyncio
from nednl import NedNL
from dotenv import load_dotenv

os.system('clear')
load_dotenv()
NED_API_KEY = os.getenv("NED_API_KEY")

async def main() -> None:
    """Fetch utilizations from the National Energy Dashboard NL."""
    api_key: str = NED_API_KEY
    async with NedNL(api_key) as client:
        utilizations = await client.utilization(
            point_id=0,
            type_id=2,
            granularity_id=3,
            granularity_timezone_id=1,
            classification_id=2,
            activity_id=1,
            start_date="2024-03-29",
            end_date="2024-03-30",
        )

        for item in utilizations:
            print(item)

        # Convert to DataFrame and print
        df = pd.DataFrame([item in utilizations])
        print(df)

if __name__ == "__main__":
    asyncio.run(main())

