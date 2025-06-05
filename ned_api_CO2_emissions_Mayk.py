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
    """Show example on using this package."""

    async with NedNL(NED_API_KEY) as client:
        response = await client.utilization(
            point_id=0,
                # Point(id=0, name='Nederland', shortname='NL')
                # Point(id=1, name='Groningen', shortname='Gr')
                # Point(id=2, name='Friesland', shortname='Fr')
                # Point(id=3, name='Drenthe', shortname='Dr')
                # Point(id=4, name='Overijssel', shortname='Ov')
                # Point(id=5, name='Flevoland', shortname='FL')
                # Point(id=6, name='Gelderland', shortname='Ge')
                # Point(id=7, name='Utrecht', shortname='Ut')
                # Point(id=8, name='Noord-Holland', shortname='No')
                # Point(id=9, name='Zuid-Holland', shortname='Zu')
                # Point(id=10, name='Zeeland', shortname='Ze')
                # Point(id=11, name='Noord-Brabant', shortname='Nb')
                # Point(id=12, name='Limburg', shortname='Li')
            type_id=2,
                # Type(id=0, name='All', shortname='All')
                # Type(id=1, name='Wind', shortname='W')
                # Type(id=2, name='Solar', shortname='S')
                # Type(id=3, name='Biogas', shortname='B')
                # Type(id=4, name='HeatPump', shortname='HP')
                # Type(id=27 is alles)
            granularity_id=6,   
                # Granularity(id=1, name='1Min')
                # Granularity(id=2, name='5Min')
                # Granularity(id=3, name='10Min')
                # Granularity(id=4, name='15Min')
                # Granularity(id=5, name='Hour')
                # Granularity(id=6, name='Day')
                # Granularity(id=7, name='Month')
                # Granularity(id=8, name='Year')
                # GranularityTimezone(id=0, name='UTC')
                # GranularityTimezone(id=1, name='Europe/Amsterdam')
            granularity_timezone_id=1,

            classification_id=2,
                # Classification(id=1, name='Forecast')
                # Classification(id=2, name='Current')
                # Classification(id=3, name='Backcast')
            activity_id=1,
                # Activity(id=1, name='Providing')
                # Activity(id=2, name='Consuming')
                # Activity(id=3, name='Import')
                # Activity(id=4, name='Export')
                # Activity(id=5, name='Storage In')
                # Activity(id=6, name='Storage Out')
                # Activity(id=7, name='Storage')
            start_date="2024-03-29",
            end_date="2024-03-30",
        )


        
    """Fetch all area points from the National Energy Dashboard NL."""
    api_key: str = "YOUR_API_KEY"
    async with NedNL(api_key) as client:
        points = await client.all_points()

        for item in points:
            print(item)




        # Parse Utilization objects into DataFrame
        df = pd.DataFrame([{
            "id": u.id,
            "capacity": u.capacity,
            "volume": u.volume,
            "percentage": u.percentage,
            "emission": u.emission,
            "emission_factor": u.emission_factor,
            "valid_from": u.valid_from,
            "valid_to": u.valid_to,
            "last_update": u.last_update
        } for u in response])
        print(df)

if __name__ == "__main__":
    asyncio.run(main())


