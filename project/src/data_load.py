import utils
import random

#reads JSON files in the folder using utils function and returns a list of patient documents as dictionaries
def read_data(folder, sample_size = 1000, seed=42):
    files_dictionary = utils.read_json_files_from_directory(folder)
    documents = list(files_dictionary.values())
    random.seed(seed)
    sample_size = min(sample_size, len(documents))
    documents = random.sample(documents, sample_size)

    return documents