class Human:

    def __init__(self,id_number:str, name:str, age: int, priority:bool, blood_type: str):
      self.id_number = id_number
      self.name =name
      self.age = age
      self.blood_type = blood_type
      self.priority = priority
      self.family = []

    def add_family_member(self, person):
        self.family.append(person)

    def __str__(self):
        return f"name: {self.name} age: {self.age} priority: {self.priority}"
    


class Queue:

    def __init__(self):
      self.waiting_humans = []

    def add_person(self,person: Human):
      if person.age > 60 or person.priority:
         self.waiting_humans.insert(0, person)
      else:
         self.waiting_humans.append(person)

    def find_in_queue(self, person: Human):
      for i in range(len(self.waiting_humans)):
         if self.waiting_humans[i].id_number == person.id_number:
            return i
      else:
        return -1 # the person is not exist at the waiting list

    def swap(self,person1: Human, person2: Human):
      person1_index = self.find_in_queue(person1)
      person2_index = self.find_in_queue(person2)

      self.waiting_humans.pop(person1_index)
      self.waiting_humans.insert(person1_index, person2)

      self.waiting_humans.pop(person2_index)
      self.waiting_humans.insert(person2_index, person1)

    def get_next(self):
      return self.waiting_humans[0]

    def get_next_blood_type(self, blood_type):
      for human in self.waiting_humans:
         if blood_type == human.blood_type:
            return human

      return None

    @staticmethod
    def get_age(person):
      return person.age

    @staticmethod
    def get_priority(person):
      return 1 if person.priority else 0

    def sort_by_age(self):
      self.waiting_humans.sort(key=Queue.get_age, reverse=True)
      self.waiting_humans.sort(key=Queue.get_priority, reverse=True)

    def __str__(self):
      lst = []
      for i in range(len(self.waiting_humans)):
         lst.append(str(self.waiting_humans[i]))

      return "\n".join(lst)

    def rearrange_queue(self):
      for i in range(len(self.waiting_humans)):
        if self.waiting_humans[i] and self.waiting_humans[i+1] in Human.family:
          self.swap(i + 1, i + 2)



Valerii = Human("111", "Valerii", 30, True, "A")
Wilson = Human("222", "Wilson", 61, False, "B")
Richard = Human("333", "Richard", 22, True, "AB")
Bob = Human("444", "Bob", 10, False, "AB")

queue = Queue()

queue.add_person(Valerii)
queue.add_person(Wilson)
queue.add_person(Richard)
queue.add_person(Bob)

print(queue.find_in_queue(Valerii))
print(queue.find_in_queue(Wilson))
print(queue.find_in_queue(Richard))
print(queue.find_in_queue(Bob))

print("before sorting")
print(queue)

print("after sorting")
queue.sort_by_age()
print(queue)
queue.swap(person1=Valerii, person2=Richard)
print("after swap")
#
print(queue.find_in_queue(Valerii))
print(queue.find_in_queue(Wilson))
print(queue.find_in_queue(Richard))