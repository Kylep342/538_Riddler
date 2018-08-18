package main

import (
  "fmt"
  "math/rand"
  "time"
)

func play() int {
  var cards []int
  for i := 0; i < 9; i++ {
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
  rand.Seed(time.Now().UTC().UnixNano())
  var wins int
  for i := 0; i < 1000000; i++ {
    wins += play()
  }
  fmt.Printf("In 1000000 games, you won %d times!\n", wins)
}
