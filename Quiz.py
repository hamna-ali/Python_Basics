# def deco(greet):
#     def wrapper():
#         print("Done with skin diagnosis model")
#         greet()
#         print("Skin type detection model is remaining")
#     return wrapper

# @deco
# def skin_diagnosis():
#     print("Skin diagnosis model made using EfficientNet-B3")

# skin_diagnosis()


# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = None
#             for i in range(times):
#                 result = func(*args, **kwargs)
               
#         return wrapper
#     return decorator

# @repeat(3)


# def greet(name, **info):
#     return f"Hey {name}, info: {info}"

# greet(name="Hamna Ali",university="PUCIT",city="Lahore")

player = {"name": "Rex", "city": "ShadowTown", "level": 4}

print(player["city"])


avatar = {}

avatar["hero_name"] = input("Hero name: ")
avatar["class"] = input("Class: ")
avatar["home"] = input("HomeTown: ")

print(avatar)
