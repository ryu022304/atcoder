package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	dn := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&dn[i])
	}
	keys := make(map[int]bool)
	res := []int{}
	for _, d := range dn {
		if _, value := keys[d]; !value {
			keys[d] = true
			res = append(res, d)
		}
	}
	fmt.Println(len(res))
}
