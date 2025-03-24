from PIL import Image
import os

image = Image.open("uno/UNOpngs.png")

total_width, total_height = image.size


num_columns = 10  
num_rows = 4      

height_of_first_4_rows = int(total_height * 0.65)  


card_width = total_width // num_columns  
card_height = height_of_first_4_rows // num_rows  

if not os.path.exists("cropped_cards"):
    os.makedirs("cropped_cards")


card_count = 0  
adjustment_factor = 15 

for row in range(num_rows): 
    for col in range(num_columns): 
        left = col * card_width
        upper = row * card_height
        right = left + card_width
        lower = upper + card_height

        offset = (row + 1) * adjustment_factor
        upper -= offset  
        lower -= offset  

        upper = max(0, upper)  
        lower = min(total_height, lower)  

        
        card = image.crop((left, upper, right, lower))

        
        card.save(f"cropped_cards/card_{card_count + 1}.png")
        card_count += 1

print(f"Cropped {card_count} cards from the first 4 rows and all 10 columns!")