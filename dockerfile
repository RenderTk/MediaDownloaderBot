FROM fedora:41

# Install necessary packages
RUN dnf update -y && \
    dnf install -y firefox ffmpeg && \
    dnf install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libpcap-devel xz-devel expat-devel gcc g++ && \
    dnf install -y python3 python3-pip python3-devel

# Create a non-root user and group
RUN groupadd -r app && \
    useradd -r -g app -m app

# Switch to the non-root user
USER app

# Set the working directory
WORKDIR /app/

# Install Playwright
RUN pip3 install --upgrade pip && \
    pip3 install playwright && \
    python3 -m playwright install

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary folders
RUN python3 scripts/create_necessary_folders.py

# Define the entry point
ENTRYPOINT [ "python3", "app.py" ]
