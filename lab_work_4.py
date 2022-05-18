class Hotel:
    def __init__(self, num_rooms):
        self._rooms = dict()
        self._room_types = ('SGL', 'DBL', 'Junior Suite', 'Suite')
        self._room_price = {'SGL': 5000, 'DBL': 7000, 'Junior Suite': 8500, 'Suite': 12000}
        for room_type in self._room_types:
            self._rooms[room_type] = [0 for _ in range(num_rooms)]
    def __check_room(self, room_type, room_id):
        if room_type not in self._room_types:
            raise RuntimeError(f'В гостинице нет типа: {room_type}')
        if room_id < 0 or room_id >= len(self._rooms[room_type]):
            raise RuntimeError(f'Некорректный id номера: {room_id}')
    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, room_type, room_id):
        self.__check_room(room_type, room_id)
        if self._rooms[room_type][room_id] == 0:
            self._rooms[room_type][room_id] = 1  # бронируем номер
        else:
            raise RuntimeError('Номер занят')
    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_type, room_id):
        self.__check_room(room_type, room_id)
        if room_type not in self._room_types:
            raise RuntimeError('Такого типа номера нет')
        self._rooms[room_type][room_id] = 0  # освобождаем номер
    def __str__(self):
        res = ''
        for room_type in self._room_types:
            res += f'Тип комнаты {room_type}:\n'
            for i in range(len(self._rooms[room_type])):
                if self._rooms[room_type][i] == 0:
                    res += f'Номер {i + 1} свободен\n'
                else:
                    res += f'Номер {i + 1} занят\n'
        return res
    def all_occupy(self):
        for room_type in self._room_types:
            self._rooms[room_type] = [1 for _ in range(len(self._rooms[room_type]))]
    def all_free(self):
        for room_type in self._room_types:
            self._rooms[room_type] = [0 for _ in range(len(self._rooms[room_type]))]
    # процент занятых комнат от общего количества комнат всех типов
    def get_occupied_ratio(self):
        occupied_total = 0
        rooms_total = 0
        for room_type in self._room_types:
            for room_status in self._rooms[room_type]:
                occupied_total += room_status
                rooms_total += 1
        return occupied_total / rooms_total * 100
    def get_revenue(self):
        revenue_total = 0
        for room_type in self._room_types:
            for room_status in self._rooms[room_type]:
                if room_status:
                    revenue_total += self._room_price[room_type]
        return revenue_total

    
hotel = Hotel(5) # в нашем отеле, например, 5 номеров
print(hotel._rooms) # смотрим номера через атрибут self.rooms
hotel.occypy('SGL', 3)
hotel.occypy('SGL', 4)
hotel.occypy('DBL', 0)
hotel.occypy('Junior Suite', 1)
hotel.occypy('Suite', 1)
try:
    hotel.occypy('DBL', 5)
except RuntimeError as e:
    print(e)
try:
    hotel.occypy('DBBL', 5)
except RuntimeError as e:
    print(e)
print(hotel._rooms)
print(hotel.get_revenue())
print(f'{hotel.get_occupied_ratio():.2f}%')
hotel.free('SGL', 3)
print(hotel._rooms)
print(hotel.get_revenue())
print(f'{hotel.get_occupied_ratio():.2f}%')
print(hotel.all_free())
print(hotel._rooms)
print(hotel.get_revenue())
print(f'{hotel.get_occupied_ratio():.2f}%')
print(hotel.all_occupy())
print(hotel._rooms)
print(hotel.get_revenue())
print(f'{hotel.get_occupied_ratio():.2f}%')
