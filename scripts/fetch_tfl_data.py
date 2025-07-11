import requests
import json

# --- Configuration ---
# IMPORTANT: Replace these with your actual TfL API credentials from Step 1.
# It's a better practice to use environment variables for keys, but for this
# initial script, we will place them here directly.
APP_ID = "14da79e5f6c143c481f1d4952b9cfcbb"  # Your Primary Key from the TfL portal
APP_KEY = "1d0c44f933544d46a6c75bf459a6b988" # Your Secondary Key from the TfL portal

# The specific bus stop we want to query.
# 490007391E is the ID for the bus stop at Oxford Circus Station / Oxford Street.
# This is a very busy, central location, making it ideal for testing.
STOP_POINT_ID = "490007391E"

# The base URL for the TfL API endpoint for StopPoint arrivals.
BASE_URL = f"https://api.tfl.gov.uk/StopPoint/{STOP_POINT_ID}/Arrivals"

def fetch_bus_data():
    """
    Fetches real-time bus arrival data for a specific stop point from the TfL API.
    """
    print(f"Fetching live data for bus stop: {STOP_POINT_ID}...")

    # --- Construct the Request ---
    # Parameters for the API request, including authentication credentials.
    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY
    }

    try:
        # --- Make the API Call ---
        # The requests library handles making the HTTP GET request.
        # We include a timeout to prevent the script from hanging indefinitely.
        response = requests.get(BASE_URL, params=params, timeout=10)

        # --- Check for Errors ---
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found, 401 Unauthorized).
        response.raise_for_status()

        # --- Process the Response ---
        # The API returns data in JSON format.
        data = response.json()

        if not data:
            print("No live data returned for this bus stop at the moment.")
            return

        # --- Print the Data ---
        # We use json.dumps for "pretty printing" the JSON output, making it readable.
        print("Successfully fetched data. Sample of the first bus arrival record:")
        print(json.dumps(data[0], indent=4))

        print(f"\nTotal upcoming bus arrivals found for stop {STOP_POINT_ID}: {len(data)}")


    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred with the request: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# --- Run the Script ---
if __name__ == "__main__":
    # This block ensures the fetch_bus_data() function is called only when
    # the script is executed directly.
    if APP_ID == "YOUR_PRIMARY_KEY" or APP_KEY == "YOUR_SECONDARY_KEY":
        print("!!! ERROR: Please replace the placeholder API credentials in the script before running.")
    else:
        fetch_bus_data()
