FROM python:3.13-slim

# System dependencies required by the .NET runtime:
# - libicu-dev: ICU for .NET globalization
# - libgdiplus: GDI+ for System.Drawing (image conversions)
# - fonts-liberation: fonts for watermark/text rendering
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libgdiplus fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
