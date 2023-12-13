# Image Downloader App

This is a web application for downloading images concurrently using asyncio and aiohttp. The app allows users to input the number of images they want to download and provide URLs for each image.

## Features

- Asynchronous image downloading using asyncio and aiohttp.
- URL validation using Pydantic.
- Supports downloading images in JPEG, PNG, and GIF formats.
- Provides a simple and interactive user interface with Streamlit.

## How to Use

1. Install the required libraries:

    ```bash
    pip install aiohttp asyncio streamlit
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Enter the number of images you want to download and provide the corresponding image URLs.

4. Click the "Download Images" button to initiate the download process.

5. The downloaded images will be saved to the specified save path.

## Configuration

- `save_path`: Update the `save_path` variable in the script to specify the local path where downloaded images will be saved.

## Dependencies

- [aiohttp](https://docs.aiohttp.org/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [streamlit](https://streamlit.io/)
- [pydantic](https://pydantic-docs.helpmanual.io/)

## Author

[Aman Singh Chauhan]
