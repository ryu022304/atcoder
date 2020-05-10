package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	tn := make([]int, N)
	xn := make([]int, N)
	yn := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&tn[i], &xn[i], &yn[i])
	}
	count := 0
	for i, t := range tn {
		if (t-(xn[i]+yn[i]))%2 == 0 && (t-(xn[i]+yn[i])) > 0 {
			count++
		}
	}
	if count == N {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
