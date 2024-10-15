from pathlib import Path

'''This sets up paths for assests used in the software.'''

#---Set File Path------------------------------------------------------------------------------#
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)