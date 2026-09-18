# This is the code for the hard black friday puzzle. 
# Create the dictionaries
man1 = {
    "shirt": "",
    "name": "",
    "deal": "",
    "discount": "",
    "age": "",
    "juice": ""
}
man2 = {
    "shirt": "",
    "name": "",
    "deal": "",
    "discount": "",
    "age": "",
    "juice": ""
}
man3 = {
    "shirt": "",
    "name": "",
    "deal": "",
    "discount": "",
    "age": "",
    "juice": ""
}
man4 = {
    "shirt": "",
    "name": "",
    "deal": "",
    "discount": "",
    "age": "",
    "juice": ""
}
man5 = {
    "shirt": "",
    "name": "",
    "deal": "",
    "discount": "",
    "age": "",
    "juice": ""
}
# ALL HINTS LISTED BELOW
# 1. The man drinking the Orange juice is exactly to the right of the man who got the 70% discount.
# 2. Keith is 45 years old.
# 3. The man who bought the TV is exactly to the left of the man wearing the Red shirt.
# 4. At the third position is the man who got the 50% discount.
# 4.Keith is next to the man wearing the White shirt.
# 5. The 25-year-old man is somewhere between the 35-year-old man and the 40-year-old man, in that order.
# 6. The man drinking Apple juice bought the Smartphone.
# 7. The 30-year-old man is exactly to the left of the man that bought the Beard trimmer.
# 8. Sean is the youngest.
# 9. The man that got the 40% discount is exactly to the right of the man who bought the Beard trimmer.
# 10. Keith is next to the 35-year-old man.
# 11. Eugene is 40 years old.
# 12. Sean is wearing the Black shirt.
# 13. At the fourth position is the man who got the biggest discount.
# 14. Dustin got 60% off.
# 15. The man drinking the Lemon juice is exactly to the right of the man drinking the Grape juice.
# 16. Keith bought a Game console.
# 17. he man who got the 80% discount is exactly to the left of the man who is wearing the Blue shirt.
# 18. The man drinking Grape juice bought the Beard trimmer.
# 19. The man wearing the Black shirt is somewhere to the right of Keith.
# 20. The man that bought the Smartphone is next to the man wearing the Black shirt.
# Create some list
men = [man1, man2, man3, man4, man5]
shirts = ["black", "blue", "green", "red", "white"]
names = ["dustin", "eugene", "hank", "keith", "sean"]
deals =["beard trimmer", "game console", "laptop", "smartphone", "tv"]
discounts = ["40%", "50%", "60%", "70%", "80%"]
ages = ["25", "30", "35", "40", "45"]
juices = ["apple", "cranberry", "grape", "lemon", "orange"]
# lets start the code here
man3["discount"] = "50%"
man4["discount"] = "80%"
man5["shirt"] = "blue"

keith_facts = ["45", "+/- white shirt", "+/- 35", "game console" ]
sean_facts = ["25", "black"]
possible_40 = [man2, man5] 



# Run this code to see the results
for number, man in enumerate(men, start=1):
    print(f"Man #{number}: {man}")