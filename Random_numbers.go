// Эта функция для создания случайного числа. Не помню уже, зачем ее делал. Возможно, чисто ради интереса. Принимает 2 числа: минимальное и максиальное значение.
// После чего выдает случайное число в этих пределах.
package main

import (
  "fmt"
  "time"
  "strconv"

)


func main () {
  number:=random_numbers(10, 60000)
  fmt.Println(number)
}

// this function take 2 random integer numbers and return 1 random number
func random_numbers (o,i int) int {
  if i-o>100 {// if number range is too big (mor than 100) it uses division for make it smaller
    o, i = division(o,i)
  }
  r:=0
  n:=""
  for w:=o; w<=i; w++{
    x:=time.Now()
    z:=x.Nanosecond()
    time.Sleep(111*time.Nanosecond) //this sleep required for z variable was not the same all the time on quick computers (to tell the truth on almost every modern computer)
    p:=strconv.Itoa(z)
    v:=p[3:6]
    if v>n {
      r=w
      n=v
    }

  }
return (r)

}
// this function is needet if we have a big range of potential numbers. It divides range by 10 each itteration. Ex we have range 10000 (from 1 to 10001), after firts itteration we will have range 1000 (ex from 7000 to 8000), after second - 100 (ex from 7500 to 7600) and so on.
func division (one, two int) (int, int) {
      np:=0
      pn:=""
      for io:=1; io<=10; io++{
        x:=time.Now()
        z:=x.Nanosecond()
        time.Sleep(111*time.Nanosecond)//sleep also required for different z variables
        p:=strconv.Itoa(z)
        v:=p[3:6]
        if v>pn {
          np=io
          pn=v
      }

}
one=one+(two-one)/10*(np-1)
two=one+(two-one)/10*np
//fmt.Println(one, two)//this print is good if you want to see division work
if (two-one)>100 {
one, two = division (one, two)
}
return one, two
}
