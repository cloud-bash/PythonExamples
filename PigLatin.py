def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + 'ay'
    say += word + " "
    # Turn the list back into a phrase
  say = say.rstrip()
    #rstrip removes the extra " " from the last iteration through the words List
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
