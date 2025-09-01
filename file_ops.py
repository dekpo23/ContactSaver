from pathlib import Path
import csv
def save_participant(path, participant_dic):
    if path.exists():
        with open(path, 'a', newline="", encoding = 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(participant_dic.values())
            
    else:
        with open(path, 'w', newline="", encoding='utf-8') as f:
            f.write('name, age, phone, track\n')
            writer = csv.writer(f)
            writer.writerow(participant_dic.values())

def load_participants(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        participant = []
        reader = csv.reader(f)
        for i, j in enumerate(reader):
            if i > 0:
                name, age, phone, track = j
                participant.append({'name': name, 'age': age, 'phone': phone, 'track': track})
    return participant

