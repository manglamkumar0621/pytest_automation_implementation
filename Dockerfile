# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
# Set the working directory in the container
RUN mkdir /pytest-container-execution/
# Create the directory (WORKDIR will create it if it doesn't exist, but explicit mkdir is fine)
WORKDIR /pytest-container-execution/
# Install system dependencies for Chrome and other tools
# This includes wget, unzip, curl, and tar for Selenium Manager,
# and other libraries Chrome needs to run headless.
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    tar \
    gnupg \
    apt-transport-https \
    ca-certificates \
    libappindicator1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgconf-2-4 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    lsb-release \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
# Install Google Chrome Stable (latest version)
# This will install the latest stable Chrome browser.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable
# Copy the entire project into the container
ADD . /pytest-container-execution/
# Copy the requirements file and install Python dependencies
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
# Set the default command to run pytest
CMD ["pytest", "-v", "--html=reports/report.html", "--self-contained-html"]
