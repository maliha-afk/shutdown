
shut=print("Are you ready to shutdown your system?")
answer=str(input("please answer here: "))
yes = "yes"
no="no"
idk ="I don't know"
if answer == yes:
  print("Did you close all the windows in your pc?")
  answer2=str(input("please answer here: "))
  if answer2 == yes:
    print("Then turn your pc off")
  elif answer2==no:
    print("Then what are you waiting for? close all the browsers!")
elif answer== idk:
  print("Then make sure to check and please check the battery while your at it")
else:
   print("then please do your job or work and ask me again when you finish and want to close your pc")