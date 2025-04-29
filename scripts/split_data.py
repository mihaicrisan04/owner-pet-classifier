import os
import shutil
import random
from pathlib import Path

# Configuration
ROOT_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OWNER_DIR = os.path.join(DATA_DIR, 'owner')
PET_DIR = os.path.join(DATA_DIR, 'pet')
ANOTHER_PERSON_DIR = os.path.join(DATA_DIR, 'another_person')

TEST_DATA_DIR = os.path.join(DATA_DIR, 'test_data')
OWNER_TEST_DIR = os.path.join(TEST_DATA_DIR, 'owner')
PET_TEST_DIR = os.path.join(TEST_DATA_DIR, 'pet')
ANOTHER_PERSON_TEST_DIR = os.path.join(TEST_DATA_DIR, 'another_person')

# Create directories if they don't exist
for directory in [OWNER_TEST_DIR, PET_TEST_DIR, ANOTHER_PERSON_TEST_DIR]:
    os.makedirs(directory, exist_ok=True)

# Split Ratio (0.2 for 20% testing, 80% training)
TEST_SPLIT_RATIO = 0.2

# Function to split data
def split_data(source_dir, test_dir, split_ratio):
    all_files = [f for f in os.listdir(source_dir) if f.endswith('.jpg')]
    random.shuffle(all_files) # shuffle the files

    num_test_files = int(len(all_files) * split_ratio)
    test_files = all_files[:num_test_files]
    train_files = all_files[num_test_files:]

    print(f"Splitting data in {source_dir}: {len(train_files)} for training, {len(test_files)} for testing.")

    # Move test files and their annotations
    for filename in test_files:
        base_name = os.path.splitext(filename)[0]
        img_path = os.path.join(source_dir, filename)
        xml_path = os.path.join(source_dir, base_name + '.xml')

        shutil.move(img_path, os.path.join(test_dir, filename))
        if os.path.exists(xml_path): # Move XML only if exists
            shutil.move(xml_path, os.path.join(test_dir, base_name + '.xml'))

    print(f"Moved {len(test_files)} image to {test_dir}")


# Perform the split
split_data(OWNER_DIR, OWNER_TEST_DIR, TEST_SPLIT_RATIO)
split_data(PET_DIR, PET_TEST_DIR, TEST_SPLIT_RATIO)

print("Data splitting complete.")
print(f"Training data remains in: {OWNER_DIR}, {PET_DIR}")
print(f"Testing data is in: {OWNER_TEST_DIR}, {PET_TEST_DIR}")