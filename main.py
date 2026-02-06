from pathlib import Path
import file_ops
import re

def localpath():
    folder = Path('participant_pkg')
    folder.mkdir(exist_ok=True)
    return folder / 'participants.csv'

def participant():
    while True:
        dic = {}
        while True:
            name = input('Enter participant\'s name here: ').strip()
            # Use regex to validate name
            if re.match(r'^[A-Za-z ]+$', name):
                dic['name'] = name
                break
            else:
                print('Please enter a valid name (alphabetic characters and spaces only)')

        while True:
            age = input('Enter participant\'s age here: ')
            try:
                age = int(age)
                if age <= 200:
                    dic['age'] = age
                    break
                else:
                    print('Enter a valid age please')
            except ValueError:
                print('Enter a valid age please')

        while True:
            phone = input('Enter participant\'s phone here: ')
            if re.match(r'^\d{11}$', phone):
                dic['phone'] = phone
                break
            else:
                print('Please enter a valid phone number (11 digits)')

        while True:
            track = input('Enter participant\'s track here: ').strip()
            if track:
                dic['track'] = track
                break
            else:
                print('Track cannot be empty')

        return dic

def participant_list(n):
    path = localpath()
    for _ in range(n):
        participant_dic = participant()
        file_ops.save_participant(path, participant_dic)

# Suggestion: Consider encrypting participant data before saving to ensure data security
def participant_details():
    path = localpath()
    return file_ops.load_participants(path)

def main():
    try:
        choice = int(input('Enter 1 to save participant details, 2 to view participants: '))
        if choice == 1:
            num_people = int(input('Enter number of participants: '))
            participant_list(num_people)
        elif choice == 2:
            print(participant_details())
    except ValueError as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
