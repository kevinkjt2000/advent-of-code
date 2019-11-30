#!/usr/bin/env bash
set -euo pipefail
day=$1

mkdir -p $year
curl -H "Cookie: session=$session" https://adventofcode.com/$year/day/$day/input > $year/day$day.input
