def main():
    with open("input-day-02.txt", 'r') as f:
        data = f.read().splitlines()

    # X for Rock, Y for Paper, and Z for Scissors
    map_items = {"X": 1, "Y": 2, "Z": 3}
    # A for Rock, B for Paper, and C for Scissors
    map_scores = {
        "A X": 3, "A Y": 6, "A Z": 0,
        "B X": 0, "B Y": 3, "B Z": 6,
        "C X": 6, "C Y": 0, "C Z": 3
    }

    # lose, draw, win
    map_outcomes = {"X": 0, "Y": 3, "Z": 6}
    # lookup by outcome
    map_outcome_items = {
        "A 0": "Z", "A 6": "Y", "A 3": "X",
        "B 0": "X", "B 3": "Y", "B 6": "Z",
        "C 6": "X", "C 0": "Y", "C 3": "Z"
    }

    score = 0
    for line in data:
        item, outcome = line.split(" ")
        outcom_score = map_outcomes[outcome]
        score += outcom_score
        item = map_outcome_items[f"{item} {outcom_score}"]
        score += map_items[item]
    print(score)


if __name__ == "__main__":
    main()
