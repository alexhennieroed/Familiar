## @module Map
#  Defines a map for use in the game


## Defines a map class
# Maps can be any size, but only 20x10 tiles will be on screen at once
class Map:
    ## Constructor
    #  @arg map_file Path to the map file
    def __init__(self, map_file):
        self.map_file = map_file
        self.tiles = parseTiles(map_file)
        return

    ## Parse the map file and turn it into a 2d array of codes
    def parseTiles(self, map_file):
        map_tiles = []
        with open(map_file, "r") as file:
            for line in file:
                line = line.strip()
                tile_codes = line.split(", ")
                tile_line = []
                for code in tile_codes:
                    tile_line.append(code)
                map_tiles.append(tile_line)
        return map_tiles
