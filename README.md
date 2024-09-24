## Overview

This is a simple Image Moderation tool to analyze images and perform content safety checks. It uses the LlaVA model for generating detailed image descriptions and the Llama Guard model for assessing content safety. The application provides a user-friendly interface built with Gradio, making it easy for users to upload images or provide image URLs for analysis.

## Features

- Image analysis using LlaVA 1.5 7B model
- Content safety check using Llama Guard 3 8B model
- Support for both image file uploads and image URLs
- User-friendly interface built with Gradio

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/lahsaini-mohammed/image-moderation.git
   cd image-moderation
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. rename `.env.example` file as `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and navigate to the URL provided in the terminal (usually `http://127.0.0.1:7860`).

3. Use the interface to upload an image file or paste an image URL.

4. Click the "Analyze Image" button to process the image.

5. View the results of the image analysis and content safety check.