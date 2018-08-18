package main

import (
  "flag"
  "fmt"
  "math/rand"
  "time"
)

func play(nums int) int {
  var cards []int
  for i := 0; i < nums; i++ {
    cards = append(cards, i+2)
  }

  var cardPos = rand.Intn(len(cards))
  var currentCard = cards[cardPos]

  cards = append(cards[:cardPos], cards[cardPos+1:]...)

  for len(cards) > 0 {
    higher := make(map[int]bool)
    lower := make(map[int]bool)
    for _, v := range cards {
      if v > currentCard {
        higher[v] = true
      } else {
        lower[v] = true
      }
    }

    var choice map[int]bool
    if len(higher) > len(lower) {
      choice = higher
    } else {
      if len(higher) == len(lower) {
        if choose := rand.Intn(2); choose == 1 {
          choice = higher
        } else {
          choice = lower
        }
      } else {
        choice = lower
      }
    }

    var nextCardPos = rand.Intn(len(cards))
    var nextCard = cards[nextCardPos]

    if choice[nextCard] {
      cards = append(cards[:nextCardPos], cards[nextCardPos+1:]...)
      currentCard = nextCard
    } else {
      return 0
    }
  }
  return 1
}

func main() {
  nums := flag.Int("nums", 9, "Number of numbered cards, starting from 2.")
  games := flag.Int("games", 1000000, "Number of games to simulate.")
  flag.Parse()

  rand.Seed(time.Now().UTC().UnixNano())

  var wins int
  for i := 0; i < *games; i++ {
    wins += play(*nums)
  }
  fmt.Printf("In %d games, you won %d times!\n", *games, wins)
}
