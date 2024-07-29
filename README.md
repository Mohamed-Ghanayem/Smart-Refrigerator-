
![MainGUI](https://github.com/user-attachments/assets/e9766369-3de8-465f-a579-9e7c42a7b761)

<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/44aaae99-c0bb-4187-9462-a4831d3f1e76" alt="Add Manually" width="350" height="300"/>
    <img src="https://github.com/user-attachments/assets/7d9b27b5-bdb0-4b2e-9d9f-4f09f0bfc55e" alt="Expired Notification" width="350" height="300"/>
    <img src="https://github.com/user-attachments/assets/ee69cd31-808f-4b61-a4dd-0ebf0d48ce3b" alt="Notifications 2" width="350" height="300"/>
</div>




## Overview

The Smart Refrigerator System is an innovative application designed to help you manage your refrigerator's contents efficiently. Using image recognition technology, this system identifies items placed in or taken out of the refrigerator, tracks their quantities, and monitors their expiration dates. The system features an intuitive graphical user interface (GUI) that allows users to interact with and manage their refrigerator's inventory seamlessly.

## Features

1. **Automatic Item Recognition**: Uses image classification algorithms to recognize items placed in or removed from the refrigerator.
2. **Inventory Management**: Tracks the quantities of items and their expiration dates.
3. **User-Friendly GUI**: Provides an intuitive interface to interact with the system, featuring buttons and lists to manage items.
4. **Customizable Lists**: Users can manage various lists such as 'In Stock', 'Expiring Soon', 'Expired', 'Default List', and 'Shopping List'.

## Hardware and Software Requirements

- **Jetson Nano**: The system runs on the Jetson Nano, a small, powerful computer designed for AI applications.
- **JetPack SDK**: Utilizes NVIDIA's JetPack SDK, which includes the necessary libraries and tools for developing AI applications on Jetson devices.
- **Image Recognition**: Leverages the image recognition algorithms from the [jetson-inference repository](https://github.com/dusty-nv/jetson-inference).

## GUI Components

### Main Buttons

- **In Button**: Initiates the process of adding a new item to the refrigerator. When pressed, the system uses image recognition to identify the item and asks the user for the quantity and expiration date.
- **Out Button**: Initiates the process of removing an item from the refrigerator. Similar to the In button, it uses image recognition and then asks the user for the quantity being removed.
- **Advanced Options Button**: Provides access to advanced management features such as viewing and managing different lists.

### Lists
![Second GUI](https://github.com/user-attachments/assets/2e2a78b7-b06e-4046-a89f-ab7d0b8686b1)

- **Default List**: Displays a predefined list of items commonly stored in the refrigerator. Users can add or delete items from this list to customize it according to their needs.
- **In Stock List**: Shows all items currently in the refrigerator, including their quantities and expiration dates.
- **Expiring Soon List**: Lists items that are nearing their expiration date. This list is updated every 10 seconds by checking the 'In Stock' list.
- **Expired List**: Contains items that have passed their expiration date.
- **Shopping List**: Allows users to manually add items they need to purchase.

### Additional Buttons

- **Confirm Button**: Confirms the recognized item and proceeds to the input windows for quantity and expiration date.
- **Decline Button**: Cancels the current operation if the recognized item is incorrect.
- **Close List Button**: Closes the currently open list and returns to the main view.

## How to Use the GUI

1. **Adding an Item**:
   - Press the **In Button**.
   - The system will use image recognition to identify the item.
   - Confirm the recognized item.
   - Enter the quantity and expiration date. You can skip these inputs if necessary.
   - The item is added to the 'In Stock' list.

2. **Removing an Item**:
   - Press the **Out Button**.
   - The system will recognize the item to be removed.
   - Confirm the recognized item.
   - Enter the quantity to be removed and the expiration date (if applicable). Skipping inputs is also possible.
   - The item is removed from the 'In Stock' list.

3. **Viewing and Managing Lists**:
   - Press the **Advanced Options Button**.
   - Select the desired list to view.
   - Use the **Close List Button** to return to the main view.

## List Updates

- **In Stock List**: Updated whenever items are added or removed.
- **Expiring Soon List**: Automatically updated based on the current date and the expiration dates of items in the 'In Stock' lis that are near their expiration date.
- **Expired List**: Automatically updated based on the current date and the expiration dates of items in the 'In Stock' list.
- **Default List**: Users can add or delete items in this list, which serves as a predefined set of items commonly stored in the refrigerator.
- **Shopping List**: Once an item expires it autmatically gets added to the Shopping list as well as when its quantity run out.

## Algorithm for Item Recognition

The system uses image classification algorithms from the [jetson-inference repository](https://github.com/dusty-nv/jetson-inference). The algorithm works as follows:

1. **Image Capture**: Captures an image of the item using the camera.
2. **Preprocessing**: Preprocesses the image to make it suitable for classification.
3. **Classification**: Uses a trained model to classify the item based on the image.
4. **Translation**: Maps the recognized item to a predefined item name using a translation list.

The `image_classification.py` script handles the image classification process, leveraging the NVIDIA Jetson Nano's capabilities to run the neural networks efficiently.

## Setup and Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/smart-refrigerator.git
   cd smart-refrigerator
   ```

## Dependencies

- Python 3.x
- tkinter
- PIL (Pillow)
- datetime
- json
- subprocess

Install all dependencies using:
```bash
pip install -r requirements.txt


2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt   #This fule include all the missing dependencies of yours, you can install them invidually
   ```

3. **Set Up Jetson Inference**:
   Follow the instructions in the [jetson-inference repository](https://github.com/dusty-nv/jetson-inference) to set up the image recognition algorithms on your Jetson Nano.

4. **Run the Application**:
   ```sh
   python3 management.py
   python3 GUI.py
   ```





