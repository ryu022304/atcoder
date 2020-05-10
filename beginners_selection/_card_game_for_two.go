package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	a := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&a[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(a)))
	var alice, bob []int
	for i := 0; i < N; i++ {
		if i%2 == 0 {
			alice = append(alice, a[i])
		} else {
			bob = append(bob, a[i])
		}
	}
	aSum := 0
	bSum := 0
	for _, a := range alice {
		aSum += a
	}
	for _, b := range bob {
		bSum += b
	}
	fmt.Println(math.Abs(float64(aSum - bSum)))
}
