package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func main(){

	// Part 1
	data, _ := ioutil.ReadFile("input.txt")
	depths := strings.Split(string(data), "\n")
	depths_int := make([]int, len(depths))

	for i, s := range depths {
    	depths_int[i], _ = strconv.Atoi(s)
	}

	curr := 1000
	count := 0
	for _,i := range depths_int{
		if i > curr{
			count++
		}
		curr = i
	}
	fmt.Println(count)

	// Part 2
	
	count = 0
	for i := 0; i < len(depths_int)-3; i++{
		window1 := depths_int[i] + depths_int[i+1] + depths_int[i+2]
		window2 := depths_int[i+1] + depths_int[i+2] + depths_int[i+3]
		if window2 > window1{
			count++
		}
	}
	fmt.Println(count)

}