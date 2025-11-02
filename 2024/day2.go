package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("day2.input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	numSafeReports := 0
	for scanner.Scan() {
		line := scanner.Text()
		inputs := strings.Split(line, " ")

		var report []int64
		for _, v := range inputs {
			num, err := strconv.ParseInt(v, 10, 64)
			if err != nil {
				log.Fatal(err)
			}
			report = append(report, num)
		}
		isSafe := isSafeReport(report)
		if isSafe {
			numSafeReports += 1
		}
	}

	fmt.Printf("part1: %d\n", numSafeReports)
}

func isSafeReport(report []int64) bool {
	n := len(report)
	isIncreasing := report[1]-report[0] > 0
	for i, v := range report {
		if i == n-1 {
			continue
		}
		dist := report[i+1] - v
		if dist == 0 || dist < -3 || dist > 3 {
			return false
		}
		if dist < 0 && isIncreasing || (dist > 0 && !isIncreasing) {
			return false
		}
	}
	return true
}
