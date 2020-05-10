package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	S := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&S[i])
	}
	count := 0
	f := false
	for {
		for i, s := range S {
			if s%2 == 0 {
				S[i] /= 2
			} else {
				f = true
			}
		}
		if f {
			break
		} else {
			count++
		}
	}
	fmt.Println(count)
}
