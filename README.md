[![GitHub issues](https://img.shields.io/github/issues/e0xextazy/dog_breeds_clf)](https://github.com/e0xextazy/dog_breeds_clf/issues)
[![GitHub license](https://img.shields.io/github/license/e0xextazy/dog_breeds_clf?color=purple)](https://github.com/e0xextazy/dog_breeds_clf/blob/main/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# dog_breeds_clf

### Everything is simple! Send a photo -> take a breed

## 👶 Dependencies
* [Python 3.8 or higher](https://www.python.org/downloads/)
* [Git SCM](https://git-scm.com/downloads)
* [Docker](https://docs.docker.com/get-docker/)

## 🛠️ Installation
* ### From GitHub
Step 1: 
```sh
git clone https://github.com/e0xextazy/dog_breeds_clf.git
```
Step 2: 
```sh
cd dog_breeds_clf
```
Step 3:
```sh
docker build -t <IMAGE_NAME> .
```
Step 4:
```sh
docker run -d -p 5000:5000 <IMAGE_NAME>
```

* ### From DockerHub
Step 1: 
```sh
docker pull mbaushenko/dog_breeds_clf:mvp
```
Step 2:
```sh
docker run -d -p 5000:5000 mbaushenko/dog_breeds_clf:mvp
```

## 🚀 Usage

* ### From GitHub/DockerHub
```sh
python3 utils/send_data.py
```

## ⚖️ License
[MIT © 2022 Mark Baushenko](https://github.com/e0xextazy/dog_breeds_clf/blob/main/LICENSE)
