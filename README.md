# Alerji AI

Alerji AI is an application that helps users detect allergenic substances by scanning product labels. It captures images from users through a SwiftUI interface, sends these images to a Python backend, and uses a custom-trained YOLOv9 model to identify the product name. The identified product name is then searched in a Firebase database, and the allergenic substances contained within the product are reported to the user.

## Features

- User Registration and Login (Firebase Authentication)
- Capture and upload photos of product labels
- Product detection using YOLOv9 model
- Integration with Firebase database
- Display of product detection results and allergen information

## Requirements

- Python 3.8 or higher
- Swift 5.0 or higher
- Xcode 12.0 or higher
- [ngrok](https://ngrok.com/)

## Installation

### Backend

1. Clone this repository:
    ```bash
    git clone https://github.com/username/AlerjiAI-python.git
    cd AlerjiAI-python
    ```
2. Clone [yolov9](https://github.com/WongKinYiu/yolov9) repository inside the project folder:
    ```bash
    cd AlerjiAI-python
    git clone https://github.com/WongKinYiu/yolov9.git
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Insert your OpenAI API `SECRET_API_KEY` in the `.env` file
   
    ```bash
    SECRET_API_KEY= Your Key here
    BASE_URL=https://api.openai.com/v1/chat/completions
    ```

5. Start the project:
    ```bash
    python main.py
    ```
   Note the URL provided by `ngrok`, as this URL will be used by the [SwiftUI application](https://github.com/CicekIbrahim/AlerjiAI).

### Frontend (SwiftUI)

1. Open Xcode and import your project.
2. Update the ngrok URL provided by the backend.
3. Run the SwiftUI application.

## Usage

1. Start the application and log in.
2. Capture or upload a photo of the product label.
3. The application will identify the product and display the allergen information.

## Note

There is an issue where the latest macOS uses the default port for Flask. To resolve it, head over to System Preferences > AirDrop & Handoff and disable the AirPlay Receiver.
