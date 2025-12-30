package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func get_rotations() []string {
	rotations, err := os.ReadFile("../input.txt")
	if err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	return strings.Split(string(rotations), "\n")

}

func rotate_dial_1(rotations []string, start int, max int) int {
	zero_count := 0
	pos := start

	for _, r := range rotations {
		if len(r) < 1 {
			break
		}
		d := r[:1]
		n, err := strconv.Atoi(r[1:])
		if err != nil {
			log.Fatalf("Error converting rotation to int: %v", err)
		}
		switch d {
		case "L":
			pos -= (n % max)
			if pos < 0 {
				pos += max
			}
		case "R":
			pos += (n % max)
			for pos >= max {
				pos -= max
			}

		}
		if pos == 0 {
			zero_count++
		}
	}

	return zero_count
}

func rotate_dial_2(rotations []string, start int, max int) int {
	zero_count := 0
	pos := start

	for _, r := range rotations {
		if len(r) < 1 {
			break
		}
		d := r[:1]
		n, err := strconv.Atoi(r[1:])
		if err != nil {
			log.Fatalf("Error converting rotation to int: %v", err)
		}
		switch d {
		case "L":
			if pos == 0 {
				zero_count--
			}
			pos -= n
			for pos < 0 {
				pos += max
				zero_count++
			}
		case "R":
			pos += n
			for pos >= max {
				pos -= max
				if pos != 0 {
					zero_count++
				}
			}

		}
		if pos == 0 {
			zero_count++
		}
	}

	return zero_count
}

func main() {
	rotations := get_rotations()
	start := 50
	max := 100
	ans := rotate_dial_1(rotations, start, max)
	fmt.Println("Part 1: ", ans)

	ans = rotate_dial_2(rotations, start, max)
	fmt.Println("Part 2: ", ans)
}
