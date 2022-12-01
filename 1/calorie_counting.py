if __name__ == "__main__":
    with open("input") as f:
        calories = []
        agg = 0
        for line in f.readlines():
            if line == "\n":
                calories.append(agg)
                agg = 0
            else:
                agg += int(line[:-1])

        sorted_calories = sorted(calories, reverse=True)

        print(f"top: {sorted_calories[0]}")
        print(f"top 3: {sum(sorted_calories[0:3])}")
