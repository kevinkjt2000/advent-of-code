#include <iostream>
#include <map>

void part1() {
	uint64_t b = 0, c = 0, d = 0, f = 0;
	uint64_t prev_d = 0;
	std::map<uint64_t, uint64_t> freqs;
	
	d = 0;
	do {
		f = d | 65536u;
		d = 5557974;
inst_08:
		c = f & 255u;
		d += c;
		d &= 16777215u;
		d *= 65899;
		d &= 16777215u;
		c = (256 > f) ? 1 : 0;
		if(c == 0) {
			c = 0;
inst_18:
			b = c + 1;
			b *= 256;
			
			b = (b > f) ? 1 : 0;
			if(b == 1) {
				f = c;
				goto inst_08;
			} else {
				c += 1;
				goto inst_18;
			}
		}
		++freqs[d];
		if(false /* part1 ? */) break;
		if(freqs[d] == 2) {
			d = prev_d;
			break;
		}
		prev_d = d;
		c = 0; // never equal to a  ->  (d == a) ? 1 : 0;
	} while(c == 0);
	std::cout << d << std::endl;
}

int main() {
	part1();
}
