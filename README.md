# Gesture Scroll Control

Gesture Scroll Control is a Python application that lets you control scrolling on your desktop using hand gestures. With a simple hand movement, you can navigate through web pages and apps without needing to touch your mouse or keyboard. It's designed for ease of use and hands-free navigation.

## Features
- **Interactive Gesture Control**: Use hand gestures to scroll up or down.
- **User-Friendly Design**: Intuitive and easy to use.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Getting Started

### Prerequisites
- **Python**: Ensure you have Python 3.7 or later installed on your computer. You can download Python from the [official website](https://www.python.org/downloads/).
- **Git**: Make sure Git is installed on your computer for cloning the repository. You can download Git from the [official website](https://git-scm.com/downloads).

### Installation Steps

1. **Clone the Repository**
   
   Open a terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/sd338/Gesture-Scroll-Control.git
   ```

   This will create a folder named `Gesture-Scroll-Control` with all the project files.

2. **Navigate to the Project Directory**

   Change to the project directory using the following command:
   ```bash
   cd path/to/Gesture-Scroll-Control
   ```

3. **Set Up a Virtual Environment (Recommended)**

   Creating a virtual environment helps manage project-specific dependencies.

   - **Windows**:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

   - **macOS/Linux**:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

4. **Install Dependencies**

   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the application, use the following command:
```bash
python main.py
```

This will activate your webcam and start recognizing hand gestures to control scrolling.

## Project Structure

- **gesture_control.py**: Handles hand gesture recognition and scrolling actions.
- **gui.py**: Contains the code for the graphical user interface.
- **LICENSE**: License file.
- **main.py**: Entry point of the application that integrates `gesture_control.py` and `gui.py`.
- **README.md**: This file.
- **requirements.txt**: Lists all the Python packages required for this project.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or find any bugs, feel free to reach out. You can find my contact information on my [GitHub profile](https://github.com/sd338).

### How to Contribute

1. **Fork the Repository**

   Click the "Fork" button at the top-right corner of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/Gesture-Scroll-Control.git
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature-or-bugfix-name
   ```

4. **Make Your Changes**

5. **Commit and Push Your Changes**

   ```bash
   git add .
   git commit -m "Description of the feature or bug fix"
   git push origin feature-or-bugfix-name
   ```

6. **Submit a Pull Request**

   Go to the original repository and click the "New Pull Request" button.

## License

MIT License

```
MIT License

Copyright (c) 2024 Samanta Das

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### Contact

For any questions or support, please connect with me on Twitter or LinkedIn. You can find links to these profiles on my [GitHub profile](https://github.com/sd338).

