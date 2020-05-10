package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var N, A, B int
	res := 0
	fmt.Scanf("%d %d %d", &N, &A, &B)
	for i := 1; i <= N; i++ {
		s := strconv.Itoa(i)
		S := strings.Split(s, "")
		temp := 0
		for _, s := range S {
			a, _ := strconv.Atoi(s)
			temp += a
		}
		if A <= temp && temp <= B {
			res += i
		}
	}
	fmt.Println(res)
}
