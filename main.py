
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

with open('./Input/Letters/starting_letter.txt') as file:
    content = file.read()
    for name in names:
        new_name = name.strip()
        new_letter = content.replace('[name]', new_name)
        with open(f'./Output/ReadyToSend/letter_invite_{new_name}.txt', mode='w') as letter:
            letter.write(new_letter)





