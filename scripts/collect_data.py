import cv2
import os
import time
from pathlib import Path

# Configuration
ROOT_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OWNER_DIR = os.path.join(DATA_DIR, 'owner')
PET_DIR = os.path.join(DATA_DIR, 'pet')
ANOTHER_PERSON_DIR = os.path.join(DATA_DIR, 'another_person')

# Add directory creation
for directory in [DATA_DIR, OWNER_DIR, PET_DIR, ANOTHER_PERSON_DIR]:
    os.makedirs(directory, exist_ok=True)


# Webcam Setup
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Data Collection Script")
print("Press 'o' to capture an image of the Owner.")
print("Press 'p' to capture an image of the Owenr's Pet.")
print("press 'a' to capture an image of Another Person.")
print("press 'q' to quit.")

# Capture loop
owner_count = 0
pet_count = 0
another_person_count = 0

# Find the next available sequence number for files
def get_next_sequence_number(directory, prefix):
    existing_files = os.listdir(directory)
    max_num = 0
    for filename in existing_files:
        if filename.startswith(prefix) and filename.endswith('.jpg'):
            try:
                num = int(filename[len(prefix):-4]) # extract the number part
                max_num = max(max_num, num)
            except ValueError:
                continue # Ignore files that don't match the pattern
    return max_num + 1

owner_count = get_next_sequence_number(OWNER_DIR, 'owner_')
pet_count = get_next_sequence_number(PET_DIR, 'pet_')
another_person_count = get_next_sequence_number(ANOTHER_PERSON_DIR, 'another_person_')

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Dsiplay the resulting frame
    cv2.imshow('Webcam Feed - Data Collection', frame)

    key = cv2.waitKey(1) & 0xFF

    # Handle key presses
    if key == ord('o'):
        # Capture Owner image
        img_name = os.path.join(OWNER_DIR, f"owner_{owner_count:03d}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Captured: {img_name}")
        owner_count += 1

    elif key == ord('p'):
        # Capture Pet image
        img_name = os.path.join(PET_DIR, f"pet_{pet_count:03d}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Captured: {img_name}")
        pet_count += 1

    elif key == ord('a'):
        # Capture Another Person image
        img_name = os.path.join(ANOTHER_PERSON_DIR, f"another_person_{another_person_count:03d}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Captured: {img_name}")
        another_person_count += 1

    elif key == ord('q'):
        # Quit the script
        break
   
# Cleanup
cap.release()
cv2.destroyAllWindows()
print("Data collection script finshed.")
