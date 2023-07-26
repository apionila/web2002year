name1 = (input("enter your name: "))
name2 = (input("enter your surname: "))
a = 0
a2 = 0
for char in name1:
    if char not in "aeiou":
        a+= 1
for char in name2:
    if char not in "aeiou":
        a2+= 1
print :(name1 {}).format(name2)
# მხოლოდ იფ გამოყენებით
# if a > a2:
#     print("xmovnebis raodenoba saxelshi metia vidre gvarshi")
# if a < a2:
#     print("xmovnebis raodenoba gvarshi ufro metia vidre saxelshi")
# if a == a2:
#     print("xmovnebis raodenoba saxelsa da gvarshi tolia")
# მეორე გზა იფ ელიფ და ელს გამოყენებით
# if a > a2:
#     print("xmovnebis raodenoba saxelshi metia vidre gvarshi")
# elif a< a2 : print("xmovnebis raodeneboa gvarshi ufro metia")
# else: print("xmovnebis raodenoba gvarshi da saxelshi tolia")
# განვიხილოთ თანხმოვნების შემთხვევა
# for char in name1:
#     if char not in "aeiou":
#         a+= 1
# for char in name2:
#     if char not in "aeiou":
#         a2+= 1
# if a > a2:
#      print("tanxmovnebis raodenoba saxelshi metia vidre gvarshi")
# if a < a2:
#      print("tamxmovnebis raodenoba gvarshi ufro metia vidre saxelshi")
# if a == a2:
#      print("tanxmovnebis raodenoba saxelsa da gvarshi tolia")
# # მეორე გზა იფ ელიფ და ელს გამოყენებით
# if a > a2:
#     print("tanxmovnebis raodenoba saxelshi metia vidre gvarshi")
# elif a< a2 : print("tanxmovnebis raodeneboa gvarshi ufro metia")
# else: print("tanxmovnebis raodenoba gvarshi da saxelshi tolia")
