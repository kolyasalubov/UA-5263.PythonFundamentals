def filter_words(st):
    return ' '.join(st.split()).capitalize()


print(filter_words('WOW this is REALLY          amazing'))
print(filter_words('HELLO CAN YOU HEAR ME'))
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))
