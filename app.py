import asyncio
import streamlit as st
from typing import List
from pydantic import BaseModel, ValidationError, validator
import aiohttp

class ImageURL(BaseModel):
    url: str

    @validator('url')
    def validate_url(cls, value):
        if not value.startswith('http'):
            raise ValueError('URL must start with http or https')
        return value

class ImageDownloader:
    def __init__(self, urls: List[str], save_path: str):
        self.urls = urls
        self.save_path = save_path

    async def download_image(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                image_format = self.get_image_format(response.headers.get('content-type'))
                if image_format:
                    filename = f"{self.save_path}/{url.split('/')[-1].split('.')[0]}.{image_format}"
                    with open(filename, 'wb') as f:
                        f.write(content)
                    st.write(f"Downloaded: {url} -> {filename}")
                else:
                    st.write(f"Skipping: {url} -> Unsupported image format")
            else:
                st.write(f"Failed to download: {url} -> HTTP Status {response.status}")

    def get_image_format(self, content_type):
        if content_type:
            if 'jpeg' in content_type.lower():
                return 'jpg'
            elif 'png' in content_type.lower():
                return 'png'
            elif 'gif' in content_type.lower():
                return 'gif'
        return None

    async def download_images(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_image(session, url) for url in self.urls]
            await asyncio.gather(*tasks)

def main():
    st.title("Image Downloader")

    # Get the number of images to download
    num_images = st.number_input("Enter the number of images to download:", min_value=1, step=1)

    # Get image URLs from the user
    image_urls = []
    for i in range(num_images):
        url = st.text_input(f"Enter URL for image {i + 1}:")
        image_urls.append(url)

    if st.button("Download Images"):
        try:
            # Validate URLs using Pydantic
            for url in image_urls:
                ImageURL(url=url)

            # Define the save path
            save_path = 'Path/for/downloaded/images'  # Update this path

            # Start the image downloader
            downloader = ImageDownloader(urls=image_urls, save_path=save_path)
            asyncio.run(downloader.download_images())

        except ValidationError as e:
            st.error(f"Validation Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")
        else:
            st.success("Download completed successfully!")

if __name__ == "__main__":
    main()
