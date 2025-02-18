PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as invitedlist: #change this to whatever path your invited_names.txt is in.
    names = invitedlist.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file: #change this to whatever path your starting_letter.txt is in.
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter: #change this to wherever you want to keep your letters.
            completed_letter.write(new_letter)
