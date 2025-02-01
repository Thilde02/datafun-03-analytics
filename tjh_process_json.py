"""
Process a JSON file to find what pt are adoptable in Montgomery County Maryland
"""


#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def count_pet_by_species(file_path: pathlib.Path) -> dict:
    """Count the number of each type if pet a JSON file."""
    try:
        with file_path.open('r') as file:
            pet_dictionary = json.load(file)  
            pet_counts_dictionary = {}
            pet_list: list = pet_dictionary.get("Animals")
            for pet_dictionary in pet_list:  
                animals = pet_dictionary.get("Animals", "Unknown")
                pet_counts_dictionary [animals] = pet_counts_dictionary.get(animals, 0) + 1
            return pet_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "astrosadoptablepets.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "json_pet_list.txt")
    
    pet_counts = count_pet_by_species(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Pet For Adoption:\n")
        for pet, count in pet_counts.items():
            file.write(f"{pet}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
