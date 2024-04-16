> [!WARNING]
> 16 april 2024: I'm archiving this repository because I don't have time to maintain it and the code, especially that of the frontend, is too outdated.

![openfish-logo-1](https://user-images.githubusercontent.com/84851956/186010813-a67bc95d-11f7-4af9-a907-806b9159618d.png)

# Seaport implementation (backend)

[Seaport](https://github.com/ProjectOpenSea/seaport) is a marketplace protocol for safely and efficiently buying and selling NFTs. This is the backend of an example implementation for educational purpose. The implementation also includes a [frontend](https://github.com/JasperAlexander/seaport-frontend).

The backend is written in Python and uses the [Django Rest Framework](https://github.com/encode/django-rest-framework). To simplify writable nested serializers package [drf-writable-nested](https://github.com/beda-software/drf-writable-nested) is being used.

## Installation

1. Install Docker.

2. Open a [Command Line Interface (CLI)](https://en.wikipedia.org/wiki/Command-line_interface) and clone this repository:

```bash
git clone https://github.com/JasperAlexander/seaport-backend.git
```

## Getting Started

1. Inside the repository, run the following command to make the docker image and run the container:

```bash
docker-compose up
```

## Contributing

Contributions are very welcome. Feel free to ask questions at the Discussions tab or reach out to one of the contributors.
