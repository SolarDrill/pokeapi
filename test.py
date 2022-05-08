mon = {"price": 0.14, "skate": False, "longboard": True}
print(mon.get('cook'))

if mon.get('cook') == None:
    mon['cook'] = True
print(mon.get('cook'))


class MON:

    def __init__(self, ojo):
        self.ojos = ojo


m = MON(3)
print(m.ojos)


variab = f"Mon tiene {m.ojos} ojos"

print(variab)