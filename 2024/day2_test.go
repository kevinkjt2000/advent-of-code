package main

import (
	"testing"
)

func TestDay2ReportSafetyPart2(t *testing.T) {
	safeReports := [][]int64{
		{7, 6, 4, 2, 1},
		{1, 3, 6, 7, 9},
		{1, 3, 2, 4, 5},
		{8, 6, 4, 4, 1},
	}
	unsafeReports := [][]int64{
		{1, 2, 7, 8, 9},
		{9, 7, 6, 2, 1},
	}

	for _, report := range safeReports {
		if !isSafeWithProblemDampnerReport(report) {
			t.Logf("report should have been safe: %v", report)
			t.Fail()
		}
	}
	for _, report := range unsafeReports {
		if isSafeWithProblemDampnerReport(report) {
			t.Logf("report should have been unsafe: %v", report)
			t.Fail()
		}
	}
}

func TestDay2ReportSafetyPart1(t *testing.T) {
	safeReports := [][]int64{
		{7, 6, 4, 2, 1},
		{1, 3, 6, 7, 9},
	}
	unsafeReports := [][]int64{
		{1, 2, 7, 8, 9},
		{9, 7, 6, 2, 1},
		{1, 3, 2, 4, 5},
		{8, 6, 4, 4, 1},
	}

	for _, report := range safeReports {
		if !isSafeReport(report) {
			t.Logf("report should have been safe: %v", report)
			t.Fail()
		}
	}
	for _, report := range unsafeReports {
		if isSafeReport(report) {
			t.Logf("report should have been unsafe: %v", report)
			t.Fail()
		}
	}
}
