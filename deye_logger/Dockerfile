ARG BUILD_ARCH
ARG BUILD_VERSION

FROM homeassistant/aarch64-base-python:latest
MAINTAINER Paul Beyleveld <paul.beyleveld@gmail.com>
LABEL io.hass.version=${BUILD_VERSION} io.hass.type="addon" io.hass.arch="${BUILD_ARCH}"

# Get the build dependencies.
RUN \
    apk add --no-cache \
        autoconf \
        automake \
        g++ \
        gcc \
        make \
        libc-dev \
        libc6-compat \
        git \
        py3-pip && \
        
        # Install requirements for add-on
        pip3 install --no-cache-dir wheel && \
        pip3 install --no-cache-dir paho-mqtt && \
        pip3 install git+https://github.com/hex-in/libscrc.git

# Clean up unnecessary build packages
RUN \
    apk del \
        autoconf \
        automake \
        g++ \
        gcc \
        make \
        libc-dev \
        git  


WORKDIR /

# Copy data for add-on
COPY DYRealTime.txt /
COPY InverterData.py /
COPY run.sh /

# set run executable
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
