import os

fn main() {
	data := os.read_file('day1.input')!
	lines := data.split('\n')
	mut total := 0
	for line in lines {
		mut num := 0
		for ch in line.split('') {
			if u8(ch[0]).is_digit() {
				num += 10 * int(ch[0] - `0`)
				break
			}
		}
		for ch in line.rsplit('') {
			if u8(ch[0]).is_digit() {
				num += int(ch[0] - `0`)
				break
			}
		}
		println(num)
		total += num
	}
	println(total)
}
