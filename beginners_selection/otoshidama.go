package main

import (
	"fmt"
)

func main() {
	var N, Y int
	fmt.Scanf("%d %d", &N, &Y)
	f := false
	for x := 0; x <= N; x++ {
		for y := 0; y <= N; y++ {
			z := N - x - y
			if z < 0 {
				break
			}
			if x*10000+y*5000+z*1000 == Y {
				fmt.Println(x, y, z)
				f = true
				break
			}
		}
		if f {
			break
		}
	}
	if !f {
		fmt.Println(-1, -1, -1)
	}
}
