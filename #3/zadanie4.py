from dataclasses import dataclass
from collections import deque
from datetime import datetime

@dataclass
class Patient:
    name: str
    surname: str
    age: int
    disease: str
    visit_time: datetime

def sort_by_visit_time(queue):
    return deque(sorted(queue, key=lambda patient: patient.visit_time))


new_queue = deque([
    Patient(name="Marek", surname="Robak", age=56, disease="Senność", visit_time=datetime(2024, 10, 25, 9, 0)),
    Patient(name="Ryszard", surname="Nowak", age=67, disease="Katar", visit_time=datetime(2024, 10, 25, 9, 20)),
    Patient(name="Jan", surname="Wydra", age=23, disease="Katar", visit_time=datetime(2024, 10, 25, 8, 0)),
    Patient(name="Władysław", surname="Młynarski", age=45, disease="Ból głowy", visit_time=datetime(2024, 10, 25, 8, 40)),
    Patient(name="Edward", surname="Bóbr", age=34, disease="Ból pleców", visit_time=datetime(2024, 10, 25, 8, 20)),
])

sorted_queue = sort_by_visit_time(new_queue)

print("---- #4 ----")
while True:
    if not sorted_queue:        
        print("Kolejka pacjentów jest pusta.")
        break

    current = sorted_queue.popleft()
    print(f"[{current.visit_time.strftime('%H:%M')}] Przyjęto: {current.name} {current.surname}({current.age}) z {current.disease}.")
    
