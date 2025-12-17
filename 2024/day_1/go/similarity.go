package main

import (
	"fmt"
)

func count(a []int, n int) int {
	count := 0
	for i := 0; i < len(a); i++ {
		if a[i] == n {
			count++
		}
	}
	return count
}

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

	similarity := 0
	
	for i := 0; i < 1000; i++ {
		similarity += left[i] * count(right, left[i])
	}
	fmt.Println(similarity)
}
