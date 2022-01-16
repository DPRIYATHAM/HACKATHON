#I am from India, here many of us give more value to emotions and relations 
#nowadys I feel bad, as they are also getting decreased.
#people are running behind money and living values and morals.
#In this process they are loosing relations and not finding anyone who can support them are help in their sadness, share their happiness.
# I want to do this project with some basic knowledge of python.
"""In India the emotions are mainly devided into 9 types and they are
Nine emotions are Shringara (love/beauty), Hasya (laughter), Karuna(sorrow), 
Raudra (anger), Veera (heroism/courage), Bhayanaka (terror/fear),
Bibhatsa (disgust), Adbutha (surprise/wonder), Shantha (peace or tranquility)"""
# when we share one of the feelings with the computer it gives a output according to that.
nam = str(input("Hi Dear user, What is your sweet name? : "))
print("What is your current emotion?"+ nam)
print("Select a emotions number from the given list")
print("For Santha(peace/tranquility) type 1")
print("For Adbutha (surprise/wonder) type 2")
print("For Bibhatsa (disgust) type 3")
print("For Bhayanaka (terror/fear) type 4")
print("For Veera (heroism/courage) type 5")
print("For Raudra (anger) type 6")
print("For Karuna(sorrow) type 7")
print("For Hasya (laughter) type 8")
print("For Shringara (love/beauty) type 9")
print("Example: If you want to input Santha(peace/tranquility) then instead of typing full name just type 1 ") 
feeling = int(input("Enter one of the specified emotion's number here : "))
if (feeling == 1):
    print("Thats really nice "+ nam + " keeping peace is a problem for many solutions. I am really happy as you are in Peace.")
elif (feeling == 2):
    print("These are common in the world "+ nam + " ,there are many wonders happening in universe at every movement, but we can't see all but if you just saw one, Congratulatins. U had a good day.")
elif (feeling == 3):
    print("I can understand the pain, but yeah still, it is life and aything can happen. We cannot change the moment " + nam + ". We are supposed to just move on. Forget the disgusting experience and move on.")
elif (feeling == 4):
    print("Ya I too get fear when ever I get a compilation error , though I am not stoped there itself "+ nam +".You just had one now, Feel free and go, just listen a song or do something you like most to do.")
elif (feeling == 5):
    print("Wow, You are noted " + nam + ". The act which you made was so courageous, you will definitely get noticed. Check some posts on socila media, you may be taggd.😊")
elif (feeling == 6):
    print("Omg I feel like a bug in my code, " + nam + ". I used that because when ever there is a bug in my code I may intended to give wrong inputs, In the same way, Anger is the most deadliest emotion in the entire list.")
    print("I suggest you to please get rid of it, It may cause severe destruction even to you are your surroundings, Keep calm. Try not be anger, We can never attain anything LongLasting with help of anger.")
elif (feeling == 7):
    print("I know how sad it will be when my coder code me with wrong syntax, " + nam + " but I never broke as I trust him, when ever he code me wrong , he corrects me or I will let him know I am in a problem. As you are coded by God, trust him or work hard, to attach your broken heart.")
elif (feeling == 8):
    print("I hope it's a good one "+ nam + ". I think your friend had been badly roasted. (Not telling you to do so.)")
    print("Laughing every day makes your day good and even your health. Keep the smile on your lips, You look too good wearing that smile.")
elif (feeling == 9):
    print("Yay, It's good " + nam + ". According to Lord Shri Krishna this feeling of the love is the oxygen to the universe, You can achieve anything with Love. I really feel happy for this emotion in you.")
else:
    print("I am sorry, " + nam + "I couldn't just get how are you feeling now, I will check my code once, meanwhile you also retype the input, from the given list.")
print("It was a good talk with you "+ nam + ". I hope my mesage got some interaction with you.")
print("Looking forward to share some more feelings with you.")
print("Have a good day "+ nam + ".")
print("Thanks for using MESHAREMO")
