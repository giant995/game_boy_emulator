from pathlib import Path

from MetaDataReader import read_cartridge_metadata

if __name__ == "__main__":
    p = Path('ROMs/snake.gb')
    print(read_cartridge_metadata(p.read_bytes()))
