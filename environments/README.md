# Environment Management

## Setting Up Environment Files

Create the required environment files from the provided examples:

```shell
cp .env.development.example .env.development  # For development
cp .env.production.example .env.production  # For production
```

> Update the respective environment variables in each file as needed.

## Managing Environments in Strapi

The application may only recognize `.env`, so depending on your environment, copy the appropriate file:

```shell
cp .env.development .env  # For development
cp .env.production .env  # For production
```

## Automating Execution

To streamline the execution process, use the following scripts:
* Development: `./run_development.sh`
* Production: `./run_production.sh`

> These scripts will automatically copy the respective environment data to `.env` and start the server.
