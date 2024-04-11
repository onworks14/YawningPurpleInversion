package main

import (
  "bufio"
  "fmt"
  "os"
  "regexp"
  "strconv"
  "strings"
)

type Line struct {
  a, b, c float64
}

type Hailstone struct {
  position [3]float64
  velocity [3]float64
}

func parseInput(line string) Hailstone {
  pattern := regexp.MustCompile(`(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)@(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)`)
  match := pattern.FindStringSubmatch(line)
  hs := Hailstone{}
  hs.position[0], _ = strconv.ParseFloat(match[1], 64)
  hs.position[1], _ = strconv.ParseFloat(match[2], 64)
  hs.position[2], _ = strconv.ParseFloat(match[3], 64)
  hs.velocity[0], _ = strconv.ParseFloat(match[4], 64)
  hs.velocity[1], _ = strconv.ParseFloat(match[5], 64)
  hs.velocity[2], _ = strconv.ParseFloat(match[6], 64)
  return hs
}

func calculateTrajectory(hs Hailstone) Line {
  var line Line
  if hs.velocity[0] == 0 {
    line.a = 0
    line.b = 1
    line.c = hs.position[0]
  } else {
    line.a = -hs.velocity[1]
    line.b = hs.velocity[0]
    line.c = line.b*hs.position[1] + line.a*hs.position[0]
  }
  return line
}

func main() {
  input := "../../txt/day24.txt"
  if len(os.Args) > 1 {
    input = os.Args[1]
  }

  file, err := os.Open(input)
  if err != nil {
    fmt.Println("Error opening file:", err)
    return
  }
  defer file.Close()

  hailstones := []Hailstone{}
  trajectories := []Line{}
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    line := strings.ReplaceAll(scanner.Text(), " ", "")
    hailstones = append(hailstones, parseInput(line))
    trajectories = append(trajectories, calculateTrajectory(hailstones[len(hailstones)-1]))
  }

  if err := scanner.Err(); err != nil {
    fmt.Println("Error reading file:", err)
    return
  }

  nIntersections := 0
  for i := 0; i < len(trajectories); i++ {
    line1 := trajectories[i]
    for j := i + 1; j < len(trajectories); j++ {
      line2 := trajectories[j]
      determinant := line1.a*line2.b - line2.a*line1.b
      if determinant == 0 {
        continue
      }
      x := (line1.c*line2.b - line2.c*line1.b) / determinant
      y := (line1.a*line2.c - line2.a*line1.c) / determinant
      if (x-hailstones[i].position[0])/hailstones[i].velocity[0] < 0 {
        continue
      }
      if (x-hailstones[j].position[0])/hailstones[j].velocity[0] < 0 {
        continue
      }
      if x >= 200000000000000 && x <= 400000000000000 && y >= 200000000000000 && y <= 400000000000000 {
        nIntersections++
      }
    }
  }
  fmt.Println(nIntersections)
}
