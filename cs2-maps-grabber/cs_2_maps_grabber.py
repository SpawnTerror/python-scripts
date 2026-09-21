import requests
from bs4 import BeautifulSoup
import re
import json

def get_steam_maps_data(collection_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(collection_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='collectionItem')
        
        # Dictionary to store the maps
        maps_dict = {}

        for item in items:
            title_div = item.find('div', class_='workshopItemTitle')
            link_tag = item.find('a', href=True)

            if title_div and link_tag:
                map_name = title_div.get_text(strip=True)
                url = link_tag['href']
                
                # Extract ID
                id_match = re.search(r'id=(\d+)', url)
                
                if id_match:
                    # Store as integer
                    maps_dict[map_name] = int(id_match.group(1))

        # --- OUTPUT 1: JSON FORMAT ---
        print("--- JSON OUTPUT ---")
        json_string = json.dumps(maps_dict, indent=4)
        print('"WorkshopMaps": ' + json_string + ',')
        
        # --- OUTPUT 2: PURE MAP:ID FORMAT ---
        print("\n--- MAP:ID LIST ---")
        for name, map_id in maps_dict.items():
            print(f"{name}:{map_id}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":

    # Surf maps link
    url = "https://steamcommunity.com/sharedfiles/filedetails/?id=3604552057"

    # KZ maps link
    # url = "https://steamcommunity.com/sharedfiles/filedetails/?id=3617299404"

    get_steam_maps_data(url)
