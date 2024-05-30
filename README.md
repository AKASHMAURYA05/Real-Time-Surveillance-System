# Real-Time Smart Surveillance System

A comprehensive real-time surveillance system featuring face recognition, face registration, motion detection (full frame and specific frame), and theft alarm triggering.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributions](#contributions)
- [Contact](#contact)

## Overview

This real-time smart surveillance system is designed to enhance security through advanced computer vision techniques. The system includes functionalities such as face recognition, person face registration, motion detection, and theft alarm triggers, providing a robust solution for modern surveillance needs.

## Features

- **Face Recognition**: Identify and verify individuals based on facial features.
- **Person Face Registration**: Register new faces into the system for recognition.
- **Motion Detection**: Detect motion within the entire frame or a specified area.
- **Theft Alarm Trigger**: Trigger alarms upon detecting suspicious activities or unauthorized access.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AKASHMAURYA05/Real-Time-Surveillance-System.git
    cd Real-Time-Surveillance-System
    ```

2. **Set up the environment**:
    - Ensure you have Python 3.8+ installed.
    - Create and activate a virtual environment:
        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Face Recognition

1. **Run the main module**:
    ```bash
    python face_recognition.py
    ```

### Person Face Registration

1. **Run the face registration module**:
    ```bash
    python face_register.py
    ```

2. **Register a new face**: Follow the on-screen instructions to capture and register new faces.

### Motion Detection

1. **Run the motion detection module**:
    ```bash
    python motion_detection.py
    ```

2. **Specify detection areas**: Configure the module to detect motion in full frame or specific regions as needed.

### Theft Alarm Trigger

1. **Run the theft alarm module**:
    ```bash
    python theft_alarm.py
    ```

2. **Set up alert mechanisms**: Configure the system to trigger alarms through various means (e.g., sound, email, SMS).

## Configuration

Adjust configuration settings in the provided configuration files:

- **config.json**: Set parameters such as camera source, detection thresholds, and alarm settings.
- **Environment variables**: Use environment variables for sensitive information like API keys and access tokens.

## Contributions

We welcome contributions to enhance the system! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

