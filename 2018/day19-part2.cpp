#include <iostream>

int main() {
	int64_t a = 0, e = 10551389, f = 1;
	while(f <= e) {
		if(e % f == 0) {
			a += f;
		}
		++f;
	}
	
	std::cout << a << std::endl;
}
