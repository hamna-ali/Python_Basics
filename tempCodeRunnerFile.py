def deco(greet):
    def wrapper():
        print("Done with skin diagnosis model")
        greet()
        print("Skin type detection model is remaining")
    return wrapper

@deco
def skin_diagnosis():
    print("Skin diagnosis model made using EfficientNet-B3")

skin_diagnosis()
