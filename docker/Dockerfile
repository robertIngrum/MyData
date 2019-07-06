# Build an image starting with the Python 3.7 image.
FROM python:3.7-alpine

# Set the working directory to /code
WORKDIR /code

# Set launch file.
ENV FLASK_APP app.py

# Install gcc so Python packages such as MarkupSafe and SQLAlchemy can compile speedups.
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements.txt and install the Python dependencies.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory . in the project to the workdir . in the image.
COPY . .

# Set the default command for the container to flask run.
CMD ["flask", "run"]
