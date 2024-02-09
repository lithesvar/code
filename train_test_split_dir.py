import os
from sklearn.model_selection import train_test_split
from shutil import copyfile

def split_dataset(input_dir, output_dir, test_size=0.2, random_state=42):
    # Create output directories if they don't exist
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # List all classes in the input directory
    classes = os.listdir(input_dir)

    for class_name in classes:
        class_path = os.path.join(input_dir, class_name)
        if os.path.isdir(class_path):
            # List all images in the class directory
            images = os.listdir(class_path)

            # Split the images into train and test sets
            train_images, test_images = train_test_split(images, test_size=test_size, random_state=random_state)

            # Copy train images to the train directory
            for train_image in train_images:
                src_path = os.path.join(class_path, train_image)
                dst_path = os.path.join(train_dir, class_name, train_image)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                copyfile(src_path, dst_path)

            # Copy test images to the test directory
            for test_image in test_images:
                src_path = os.path.join(class_path, test_image)
                dst_path = os.path.join(test_dir, class_name, test_image)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                copyfile(src_path, dst_path)

if __name__ == "__main__":
    input_directory = r'D:\computer_vission\pyimage_search\projects\first_cnn\dataset\animals'
    output_directory = r'D:\computer_vission\pyimage_search\projects\first_cnn\dataset\output_train'

    split_dataset(input_directory, output_directory, test_size=0.2, random_state=42)
