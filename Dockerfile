FROM python:3.13-slim

# System dependencies required by the .NET runtime:
# - libicu-dev: ICU for .NET globalization
# - fontconfig + fonts-liberation: font cache tooling plus metric-compatible
#   substitutes for Arial/Times/Courier
# - ttf-mscorefonts-installer: the actual Microsoft core fonts (Arial etc.),
#   which the conversion engine looks up by name for watermarks and text
#   rendering. It lives in Debian "contrib" (not enabled on the slim base
#   image), so that component is enabled first; the debconf line pre-accepts
#   its EULA and wget is needed for its font download.
#
# libgdiplus is deliberately NOT installed. Up to 26.5 the engine depended on
# System.Drawing.Common, which needs GDI+; from 26.9 (engine 26.8, .NET 10) the
# cross-platform build drops that dependency for SkiaSharp + Aspose.Drawing, and
# the Linux wheel ships no System.Drawing.Common.dll at all. Measured in this
# image: with libgdiplus present and absent the results are identical.
RUN set -eux; \
    if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
        sed -i 's/^Components: main$/Components: main contrib/' /etc/apt/sources.list.d/debian.sources; \
    else \
        sed -i 's/ main$/ main contrib/' /etc/apt/sources.list; \
    fi; \
    apt-get update -qq; \
    echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections; \
    apt-get install -y --no-install-recommends \
        libicu-dev fontconfig fonts-liberation wget ttf-mscorefonts-installer; \
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
