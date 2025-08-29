from pathlib import Path
import file_ops

def localpath():
    folder = Path('participant_pkg')
    return folder / 'participants.csv'

def participant():
    while True:
        dic = {}
        while True:
            j = True
            name = input('Enter participant\'s name here: ')
            if ' ' in name:
                for i in name.split(' '):
                    if i.isalpha() == False:
                        j = False
                if  j == True:
                    dic['name'] = name
                    break
            else:
                name = name.strip()
                if name.isalpha():
                    dic['name'] = name
                elif len(name) == 0:
                    print('Name cannot be empty') 
                else:
                    print('Please enter correct name')

        
        while True:
            age = input('Enter participant\'s age here: ')
            try:
                age = int(age)
                if age <= 200:
                    dic['age'] = age
                    break
                else:
                    print('Enter correct age please')
            except ValueError as e:
                 print('Enter  correct age please')
                
        while True:
            phone = input('Enter participant\'s phone here: ')
            if len(phone) == 11 and phone.isdigit():
                dic['phone'] = phone
                break
            else:
                print('Please enter correct phone number')
        while True:
            track = input('Enter participant\'s track here: ')
            if track.isdigit():
                print('Enter correct track please')
            elif len(track) == 0:
                print('Track cannot be empty') 
            else:
                dic['track'] = track
                break
        return dic

def participant_list(n):
    path = localpath()
    for i in range(n):
        participant_dic = participant()
        file_ops.save_participant(path, participant_dic)

def participant_details():
    path = localpath()
    return file_ops.load_participants(path)
    


def main():
    try:
        choice = int(input('Enter 1 to save participant details, 2 to view participants: '))
        if choice == 1:
            num_people = int(input('Enter number of participants'))
            participant_list(num_people)
        elif choice == 2:
            print(participant_details())
    except ValueError as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
        


