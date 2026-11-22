def calculate_number_of_characters(string):
   if not isinstance(string, str):
      raise ValueError("All elements in the string must be characters.")
   number_of_characters = {};
   number = 0;
   for character in string:
       number += 1;
       number_of_characters[character] = number_of_characters.get(character, 0) + 1
   return number_of_characters

print(calculate_number_of_characters("hello"))