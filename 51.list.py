numbers = [1,2,3,1440,5,6]
print(f"Numbers List: {numbers[3]}\n")

names = ['Hena', 'Enamul', 'Imdad', 'Shampa', 'Israt Jahan Maisha']
print(f"Names List: {names[:2]}\n") #How many items we want to see from the list

names_numbers = ['Hena','Enamul','Imdad','Shampa','Maisha',1,2,3,1440,5,6]
print(f"From Names & Numbers List: {names_numbers[-1]}\n") #print the last item

names_numbers[1]="ImdaduL Haque"
print(f"New names_numbers List: {names_numbers}\n")
