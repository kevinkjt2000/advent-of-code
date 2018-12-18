#include <fstream>
#include <iostream>
#include <vector>

const char OPEN = '.';
const char TREE = '|';
const char LUMBERYARD = '#';

struct ForestGame {
	std::vector< std::string > grid;

	void step_simulation(int num_generations) {
		for(; num_generations > 0; --num_generations) {
			std::vector< std::string > swap_grid = grid;
			for(std::size_t y = 0; y < grid.size(); ++y) {
				for(std::size_t x = 0; x < grid[y].size(); ++x) {
					int num_adj_trees = 0;
					int num_adj_lumberyards = 0;
					for(int dy = -1; dy <= 1; ++dy) {
						for(int dx = -1; dx <= 1; ++dx) {
							if((dy != 0 || dx != 0) &&
									0 <= y + dy && y + dy < grid.size() &&
									0 <= x + dx && x + dx < grid[y+dy].size()) {
								switch(swap_grid[y+dy][x+dx]) {
									case TREE: num_adj_trees++; break;
									case LUMBERYARD: num_adj_lumberyards++; break;
								}
							}
						}
					}

					switch(grid[y][x]) {
						case OPEN:
							// An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
							if(num_adj_trees >= 3) {
								grid[y][x] = TREE;
							}
							break;
						case TREE:
							// An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
							if(num_adj_lumberyards >= 3) {
								grid[y][x] = LUMBERYARD;
							}
							break;
						case LUMBERYARD:
							// An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
							if(num_adj_trees < 1 || num_adj_lumberyards < 1) {
								grid[y][x] = OPEN;
							}
							break;
					}
				}
			}
		}
	}
	
	long calculate_resource_value() const {
		long num_trees = 0;
		long num_lumberyards = 0;
		for(auto&& row : grid) {
			for(auto&& c : row) {
				if(c == TREE) { num_trees++; }
				else if(c == LUMBERYARD) { num_lumberyards++; }
			}
		}
		return num_trees * num_lumberyards;
	}

	explicit ForestGame(std::string const& filename) {
		std::ifstream file(filename);
		for(std::string line; std::getline(file, line);) {
			grid.push_back(line);
		}
	}

	friend std::ostream& operator<<(std::ostream& out, ForestGame const& fg);
};

std::ostream& operator<<(std::ostream& out, ForestGame const& fg) {
	for(auto&& row : fg.grid) {
		out << row << "\n";
	}
	return out;
}

int main() {
	ForestGame fg("day18.input");
	for(int i = 0; i < 1000; i++) {
		fg.step_simulation(1);
		std::cout << fg.calculate_resource_value() << "\n";
	}
	return 0;
}
