# MySEOToll

MySEOToll is a web application that utilizes the YouTube API to analyze video data and suggest title optimizations.

## Table of Contents
- [Requirements](#requirements)
- [YouTube API Key](#youtube-api-key)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Accessing the Application](#accessing-the-application)


### Requirements
### Installing Python3 and Pip

This guide provides instructions for installing Python3 and Pip on both Windows and Linux.

### Installation on Windows

1. **Download Python:**
   - Visit the [official Python website](https://www.python.org/downloads/).
   - Click on the "Download Python" button for the latest version.

2. **Run the Installer:**
   - Locate the downloaded file and double-click it to run the installer.

3. **Setup Options:**
   - **Important:** Check the box that says "Add Python to PATH."
   - Select "Install Now" or "Customize Installation" if you want to choose specific features.

4. **Verify Installation:**
   - Open the Command Prompt by pressing `Win + R`, typing `cmd`, and hitting Enter.
   - Type the following commands to verify Python and Pip installation:
     ```bash
     python --version
     pip --version
     ```

### Installation on Linux

1. **Update Package List:**
   - Open the terminal and run the following command to update the package list:
     ```bash
     sudo apt update
     ```

2. **Install Python3:**
   - Run the following command to install Python3:
     ```bash
     sudo apt install python3 python3-venv python3-pip
     ```

3. **Verify Installation:**
   - After the installation is complete, verify it by running:
     ```bash
     python3 --version
     pip3 --version
     ```

### Additional Steps

- **Set Environment Variables on Windows (if needed):**
  - Search for "Environment Variables" in the Start menu.
  - Click on "Edit the system environment variables."
  - In the System Properties window, click on "Environment Variables."
  - Under "User variables," click "New" to create a new variable, and add the variable name and value.


Before running the application, make sure to install the necessary dependencies. You can create a virtual environment and install the requirements using the following commands:
### For window
```
myenv/bin/activate
pip install -r requirements.txt
```
### For linux
```
source myenv/bin/activate
pip install -r requirements.txt
```

## YouTube API Key
To obtain your YouTube API key, follow these steps:

1. Go to the [YouTube Developer Console](https://developers.google.com/youtube/v3/getting-started).
2. Create a new project or select an existing one.
3. Enable the YouTube Data API v3.
4. Navigate to "Credentials" and create a new API key.

## Installation

To clone this repository, use the following command:

### For Windows/Linux
```
git clone https://github.com/gh4reeb/myseotoll.git
```
Once cloned, navigate into the project directory:
```
cd myseotoll
```

## Configuration
Before running the application, you need to configure the YouTube API key. Open the api_service.py file and change the API_KEY variable on line 5:
```
API_KEY = 'ADD_YOUR_YOUTUBE_API'
```
Replace it with your actual API key, for example:
```
API_KEY = 'AIzaSyCXG6v5qLH4Dn6KeCJ3_4vIGMAmeRkwerwer'
```
## Running the Application
After configuring the API key and installing the requirements, run the application using:
```
python3 main.py
```
## Accessing the Application
Once the application is running, you can access it in your browser at:
http://127.0.0.1:5000/

