FROM python:3.13-slim

# System dependencies required by the .NET runtime:
# - libicu-dev: ICU for .NET globalization
# - libgdiplus: GDI+ for System.Drawing (image conversions)
# - fontconfig + fonts-liberation: font cache tooling plus metric-compatible
#   substitutes for Arial/Times/Courier
# - ttf-mscorefonts-installer: the actual Microsoft core fonts (Arial etc.),
#   which the conversion engine looks up by name for watermarks and text
#   rendering. It lives in Debian "contrib" (not enabled on the slim base
#   image), so that component is enabled first; the debconf line pre-accepts
#   its EULA and wget is needed for its font download.
RUN set -eux; \
    if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
        sed -i 's/^Components: main$/Components: main contrib/' /etc/apt/sources.list.d/debian.sources; \
    else \
        sed -i 's/ main$/ main contrib/' /etc/apt/sources.list; \
    fi; \
    apt-get update -qq; \
    echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections; \
    apt-get install -y --no-install-recommends \
        libicu-dev libgdiplus fontconfig fonts-liberation wget ttf-mscorefonts-installer; \
    fc-cache -f; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
