def greeting(name):
    return 'Hola {}'.format(name)

print(greeting('Miguel'))


# def falling_speed(init_vel, time):
#     return init_vel + time * 9.81

def falling_speed(init_vel, time, gravity=9.81):
    return init_vel + time * gravity

print(falling_speed(0, 3))
print(falling_speed(0, 3, 1.622))
