FROM arm32v7/python:3.9-slim

#Download gpio lib
RUN apt-get update && \
    apt-get install -y \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY button_check.py /app/

#Run script
CMD ["python3", "button_check.py"]
