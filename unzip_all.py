import os
import zipfile
from pathlib import Path
from tqdm import tqdm

def unzip_all(root_dir):
    # Convert to Path object if string is provided
    root_dir = Path(root_dir)
    
    # Find all zip files recursively
    zip_files = list(root_dir.rglob("*.zip"))
    
    print(f"Found {len(zip_files)} zip files")
    
    # Process each zip file
    for zip_path in tqdm(zip_files, desc="Unzipping files"):
        try:
            # Extract the zip file to its parent directory
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(zip_path.parent)
                
        except Exception as e:
            print(f"Error extracting {zip_path}: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Unzip all ZIP files in directory and subdirectories")
    parser.add_argument("root_dir", type=str, help="Root directory to search for ZIP files")
    args = parser.parse_args()
    
    unzip_all(args.root_dir)
