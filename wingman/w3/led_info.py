from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    print ('Serial: {}'.format(bstick.get_serial()))
