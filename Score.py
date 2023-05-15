import Utils


def read_current_score(file_name):
    try:
        with open(file_name, 'r') as f:
            current_score = int(f.read())
            print(f"Previous total score: {current_score}")
            return current_score
    except FileNotFoundError:
        print("No previous score found.")
        return 0


def write_new_score(file_name, new_score):
    with open(file_name, 'w') as f:
        f.write(str(new_score))
    print(f"Updated total score is: {new_score}")


def add_score(difficulty):
    # Get the file name
    file_name = Utils.SCORES_FILE_NAME
    # Read current score
    current_score = read_current_score(file_name)
    # Calculate new score
    new_score = current_score + (difficulty * 3 + 5)
    # Update new score
    write_new_score(file_name, new_score)
