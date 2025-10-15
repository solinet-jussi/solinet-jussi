# Course task: A5_T4 Multiple parameter

def askDimension(PPrompt: str) -> float:
	Feed = input(f"Insert {PPrompt}: ")
	return float(Feed)

print("Program starting.")
Width = askDimension("width")
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
	return PWidth * PHeight

Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}²")
print("Program ending.")

