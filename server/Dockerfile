      
Add Dockerfile
Create a Dockerfile in the root directory. The file will have the following steps listed:

Add base image.
Add requirements.txt file.
Install and update Python.
Change working directory.
Expose port.
Run command to start application.
Here is an example file to get you started:

    FROM python:3.8.2

    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYTECODE 1

    RUN apt-get update \
        && apt-get install -y netcat

    ENV APP=/app

    # Change the workdir.
    WORKDIR $APP

    # Install the requirements
    COPY requirements.txt $APP
    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt

    # Copy the rest of the files
    COPY . $APP

    EXPOSE 8000

    RUN chmod +x /app/entrypoint.sh
    ENTRYPOINT ["/app/entrypoint.sh"]

    CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]