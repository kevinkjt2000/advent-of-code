package main

import (
	"bufio"
	"cmp"
	"fmt"
	"log"
	"math"
	"os"
	"slices"
)

func main() {
	file, err := os.Open("day1.input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var xs, ys []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var x, y int
		fmt.Sscanf(line, "%d %d", &x, &y)
		xs = append(xs, x)
		ys = append(ys, y)
	}

	slices.SortFunc(xs, func(a int, b int) int {
		return cmp.Compare(a, b)
	})
	slices.SortFunc(ys, func(a int, b int) int {
		return cmp.Compare(a, b)
	})

	totalDistance := 0
	for i := range xs {
		totalDistance += int(math.Abs(float64(xs[i] - ys[i])))
	}
	fmt.Printf("part1: %d\n", totalDistance)

	counts := make(map[int]int)
	for _, v := range ys {
		counts[v] += 1
	}

	similarityScore := 0
	for _, v := range xs {
		similarityScore += v * counts[v]
	}
	fmt.Printf("part2: %d\n", similarityScore)
}
