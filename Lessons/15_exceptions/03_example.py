class DB:
    connections = 0

    def __init__(self, cid):
        self.cid = cid
        print("Открытие соединения {}".format(self.cid))
        DB.connections += 1

    def get_data(self):
        return "Данные из соединения {}".format(self.cid)

    def close(self):
        print("Закрытие соединения {}".format(self.cid))
        DB.connections -= 1

c1 = DB(10)
c2 = DB(20)

print("----Соединений: ", DB.connections)

print(c1.get_data())
print(c2.get_data())

c1.close()
c2.close()

print("----Соединений: ", DB.connections)