//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: IntegerPower
@time: 2020/12/29 19:06
@IDE: GoLand
@desc: 数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
输入
2,3
返回值
8.00000
*/

package main

import "fmt"

// 方法一、循环
func Power( base float64 ,  exponent int ) float64 {
	//var f_exp = float64(exponent)
	var pow = base
	if exponent > 0 {
		for i := 0; i < exponent-1; i ++ {
			pow *= base
		}
		return pow
	}else if exponent < 0 {
		for i := 0; i < -exponent+1; i ++ {
			pow /= base
		}
		return pow
	}else{
		return 1
	}
}

// 方法二、递归
func Power1( base float64 ,  exponent int ) float64 {
	if exponent < 0 {
		// m 的 -n 次方 ===> 1/m 的 n 次方
		return Power1(float64(1)/base, -1 * exponent)
	}else if exponent == 1 {
		return base
	}
	return base * Power1(base, exponent-1)
}

func main() {
	var base = float64(2)
	var exponent = -2
	//power := Power(base, exponent)
	power := Power1(base, exponent)
	fmt.Printf("%f ---- %T", power, power)
}