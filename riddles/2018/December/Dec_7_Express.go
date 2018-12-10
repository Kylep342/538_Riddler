/**
Riddler Express - December 7, 2018

From Josh Vandenham, precipitation permutations:

Louie walks to and from work every day. In his city, there is a 50
percent chance of rain each morning and an independent 40 percent
chance each evening. His habit is to bring (and use) an umbrella if
it’s raining when he leaves the house or office, but to leave them all
behind if not. Louie owns three umbrellas.

On Sunday night, two are with him at home and one is at his office.
Assuming it never starts raining during his walk to his home or office,
what is the probability that he makes it through the work week without
getting wet?

Solution by Kyle Pekosh https://github.com/Kylep342
*/

package main

import (
  "flag"
  "fmt"
  "math/rand"
  "time"
)


func rainForecast(weight int) bool {
  var key = rand.Intn(10)

  switch {
  case key < weight:
    return false
  default:
    return true
  }
}

func walk(weight int, startUmbrellas []int, endUmbrellas []int) (bool, []int, []int) {
  var rain = rainForecast(weight)
  if rain {
    if len(startUmbrellas) == 0 {
      return false, startUmbrellas, endUmbrellas
    }
    startUmbrellas = startUmbrellas[:len(startUmbrellas)-1]
    endUmbrellas = append(endUmbrellas, 1)
  }
  return true, startUmbrellas, endUmbrellas
}

func simulateWeek() int {
  var homeUmbrellas = []int{1, 1}
  var workUmbrellas = []int{1}
  var dryMorning, dryEvening bool

  for i := 0; i < 5; i++ {
    dryMorning, homeUmbrellas, workUmbrellas = walk(5, homeUmbrellas, workUmbrellas)
    if !dryMorning {
      return 0
    }
    dryEvening, workUmbrellas, homeUmbrellas = walk(6, workUmbrellas, homeUmbrellas)
    if !dryEvening {
      return 0
    }
  }
  return 1
}

func main() {
  weeks := flag.Int("weeks", 1000000, "The number of weeks to simulate")
  flag.Parse()

  rand.Seed(time.Now().UTC().UnixNano())

  dryWeeks := 0
  for week := 0; week < *weeks; week++ {
    dryWeeks += simulateWeek()
  }
  accuracy := (float64(dryWeeks*100) / float64(*weeks))
  fmt.Printf("Trials: %d\nDry Weeks: %d\nP(dry): %f%%", *weeks, dryWeeks, accuracy)
}
