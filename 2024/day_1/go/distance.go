package main

import (
	"fmt"
	"slices"
)

func main() {
	a := []int{}
	for i := 0; i < 2000; i++ {
		var n int
		fmt.Scan(&n)
		a = append(a, n)
	}
	left := []int{}
	right := []int{}

	for i := 0; i < 1000; i++ {
		left = append(left, a[2 * i])
		right = append(right, a[1 + (2 * i)])
	}
	slices.Sort(left)
	slices.Sort(right)

	distance := 0
	
	for i := 0; i < 1000; i++ {
		distance += intAbs(left[i], right[i])
	}
	fmt.Println(distance)
}

func intAbs(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}
