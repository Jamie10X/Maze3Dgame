def load_map_data():
    """Load map data from 'map-data' file."""
    with open("resources/map-data", "r") as f:
        for line in f.readlines():
            split_line = line.split(";")
            start = split_line[1].split(",")
            angle = float(split_line[2])
            floor = tuple(map(int, split_line[3].split(",")))
            sky = split_line[4]
            raw_map = split_line[6]

            # Parse grid data
            mini_map = []
            for raw_row in raw_map.split("|"):
                row = [int(cell) for cell in raw_row.split(",")]
                mini_map.append(row)

            # Return the first map only
            return {
                "start": (float(start[0]), float(start[1])),
                "angle": angle,
                "floor": floor,
                "sky": sky,
                "mini_map": mini_map,
            }


class Map:
    def __init__(self):
        """Initialize the map with data from 'map-data'."""
        map_data = load_map_data()
        self.grid = map_data["mini_map"]
        self.player_start = map_data["start"]
        self.player_start_angle = map_data["angle"]
        self.sky = map_data["sky"]
        self.floor = map_data["floor"]
        self.world_map = self.build_world_map()

    def build_world_map(self):
        """Convert grid into a dictionary of walls and exit."""
        world_map = {}
        for j, row in enumerate(self.grid):
            for i, cell in enumerate(row):
                if cell:  # Add all non-zero tiles (walls, exit, etc.)
                    world_map[(i, j)] = cell
        return world_map