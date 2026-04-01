# notes for installing docker on an apt based linux workstation

from: https://docs.docker.com/engine/install/ubuntu/

## Setup the apt repository

```
./repo.sh
```

## Install the packages

```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## make sure it starts

```
sudo systemctl status docker
sudo systemctl start docker
```

