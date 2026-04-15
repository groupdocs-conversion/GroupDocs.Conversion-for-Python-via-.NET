FROM python:3.13-slim

# ICU is the only system dependency required by the .NET runtime
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
