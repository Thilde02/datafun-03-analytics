"""
This file fetches an Excel file from the web 
and saves it to a local file named Popular_Bab_Name.cvs in a folder named data.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "data"

#####################################
# Define Functions
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.

    Returns:
        None

    Example:
        fetch_csv_file("data", "data.csv", "https://example.com/data.csv")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write CVS data to the file

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): CVS content as a string

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CVS data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CVS data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CVS data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():

    csv_url = 'https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b'
    logger.info("Starting CSV fetch...")
    fetch_csv_file(fetched_folder_name, "Popular_Baby_Names.cvs", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()