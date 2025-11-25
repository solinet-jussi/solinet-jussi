# Course task: A8_T6 Scalable Vector Graphics

from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing) -> None:
	print("Insert square")
	left_pos = int(input("- Left edge position: "))
	top_pos = int(input("- Top edge position: "))
	side_length = int(input("- Side length: "))
	fill_color = input("- Fill color: ")
	stroke_color = input("- Stroke color: ")
	
	square = Rect(insert=(left_pos, top_pos), size=(side_length, side_length), 
	              fill=fill_color, stroke=stroke_color)
	PDwg.add(square)
	return None

def drawCircle(PDwg: Drawing) -> None:
	print("Insert circle")
	center_x = int(input("- Center X coord: "))
	center_y = int(input("- Center Y coord: "))
	radius = int(input("- Radius: "))
	fill_color = input("- Fill color: ")
	stroke_color = input("- Stroke color: ")
	
	circle = Circle(center=(center_x, center_y), r=radius, 
	                fill=fill_color, stroke=stroke_color)
	PDwg.add(circle)
	return None

def saveSvg(PDwg: Drawing) -> None:
	filename = input("Insert filename: ")
	print(f'Saving file to "{filename}"')
	proceed = input("Proceed (y/n)?: ")
	
	if proceed.lower() == "y":
		# Save with pretty formatting (2 space indentations)
		PDwg.saveas(filename, pretty=True)
		print("Vector saved successfully!")
	else:
		print("Save cancelled.")
	return None

def display_menu() -> None:
	print("Options:")
	print("1 - Draw square")
	print("2 - Draw circle")
	print("3 - Save svg")
	print("0 - Exit")

def main() -> None:
	print("Program starting.")
	Dwg = Drawing()
	
	while True:
		display_menu()
		choice = input("Your choice: ")
		
		if choice == "1":
			drawSquare(Dwg)
		elif choice == "2":
			drawCircle(Dwg)
		elif choice == "3":
			saveSvg(Dwg)
		elif choice == "0":
			print("Exiting program.")
			break
		else:
			print("Unknown option!")
	
	print("Program ending.")
	return None

if __name__ == "__main__":
	main()
