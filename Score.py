import Utils


def add_score(difficulty):
    file_name = Utils.SCORES_FILE_NAME
    try:
        # Try to read the current score from the file
        with open(file_name, 'r') as f:
            current_score = int(f.read())
            print(f"Previous total score: {current_score}")
    except FileNotFoundError:
        # If the file doesn't exist, create a new one with a starting score of 0
        current_score = 0
        with open(file_name, 'w') as f:
            f.write(str(current_score))

    # Calculate the new score and update the file
    new_score = current_score + ((difficulty * 3) + 5)
    print(f"Updated total score is: {new_score}")
    with open(file_name, 'w') as f:
        f.write(str(new_score))

