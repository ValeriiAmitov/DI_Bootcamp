class Door:
	def __init__(self, is_opened: bool):
		self.is_opened = is_opened

	def open_door(self):
		print('opining the door')
		self.is_opened = True

	def close_door(self):
		print('closing the door')
		self.is_opened = False


class BlockedDoor(Door):

	def open_door(self):
		raise Exception("cant open the door")

	def close_door(self):
		raise Exception("cant close the door")


door = Door(is_opened=True)
print(door.is_opened)

door.close_door()
print(door.is_opened)


door.open_door()
print(door.is_opened)

blocked_door = BlockedDoor(is_opened=False)
# blocked_door.open_door()
blocked_door.close_door()