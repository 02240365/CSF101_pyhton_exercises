#18
name = "Sonam Zangmo"
age = 18
height = 1.62
is_student = True

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)



#19
person_info ["favorite_color"] = "black"
print(person_info)



#20
try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")
    