import os
import numpy as np
from PIL import Image

def create_indexed_folders_and_convert(source_dir, destination_dir):
    """
    Creates indexed folders and converts files in the source directory.

    Args:
        source_dir: The directory containing the .npy files.
        destination_dir: The directory where the indexed folders and converted files will be created.
    """

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".npy"):
                # Extract the image number
                image_number = file.split("_")[0]
                
                # Create the indexed folder
                folder_path = os.path.join(destination_dir, image_number)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Source and destination paths
                source_path = os.path.join(root, file)
                
                # Convert based on file type
                if "input" in file:
                    # Convert to PNG
                    data = np.load(source_path)
                    img = Image.fromarray(data)
                    destination_path = os.path.join(folder_path, file.replace(".npy", ".png"))
                    img.save(destination_path)
                else:
                    # Keep as text
                    destination_path = os.path.join(folder_path, file.replace(".npy", ".txt"))
                    data = np.load(source_path)
                    with open(destination_path, "w") as f:
                        for item in data:
                            f.write(str(item) + "\n")

if __name__ == "__main__":
    source_directory = "results"
    destination_directory = "results_txt"

    create_indexed_folders_and_convert(source_directory, destination_directory)