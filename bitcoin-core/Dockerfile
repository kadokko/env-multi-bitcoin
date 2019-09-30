FROM ubuntu:bionic

ENV DEBCONF_NOWARNINGS yes
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update  -y \
&&  apt-get upgrade -y \
&&  apt-get clean

RUN apt-get install -y      \
    git                     \
    build-essential         \
    libtool                 \
    autotools-dev           \
    automake                \
    pkg-config              \
    libssl-dev              \
    libevent-dev            \
    bsdmainutils            \
    python3                 \
    libboost-all-dev        \
    libgmp-dev              \
    gmp-doc                 \
&&  apt-get clean

RUN apt-get install -y \
    software-properties-common \
&&  add-apt-repository ppa:bitcoin/bitcoin \
&&  apt-get update  -y \
&&  apt-get install -y \
    libdb4.8-dev       \
    libdb4.8++-dev     \
&&  apt-get clean

RUN apt-get install -y \
    jq                 \
    wget               \
    curl               \
    tar                \
    unzip              \
    sudo               \
    iputils-ping       \
    net-tools          \
    bc                 \
    vim-common         \
&&  apt-get clean

ARG BITCOIN_VER
RUN wget -q https://bitcoin.org/bin/bitcoin-core-${BITCOIN_VER}/bitcoin-${BITCOIN_VER}-x86_64-linux-gnu.tar.gz \
&&  tar -xzf bitcoin-${BITCOIN_VER}-x86_64-linux-gnu.tar.gz \
&&  rm -f bitcoin-${BITCOIN_VER}-x86_64-linux-gnu.tar.gz \
&&  mv /bitcoin-${BITCOIN_VER} /bitcoin

RUN mkdir -p /root/.bitcoin
ADD conf/bitcoin.conf /root/.bitcoin/.
ENV PATH $PATH:/bitcoin/bin

EXPOSE 18332

CMD ["tail", "-f", "/dev/null"]
