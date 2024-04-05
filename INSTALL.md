# Install
You'll need to go through all of the steps outlined in [CONTRIBUTING.md](CONTRIBUTING.md) to get your local environment set up. This includes installing Poetry, Make, and npx.

# Bootstrapping
Bootstrap your environments. This project is set up to deploy to a dev account from your local machine. It also uses an Operations account for initializing a Code Pipeline, a Staging account for testing changes, and a Production account for...production. You need to bootstrap each of these environments:

```bash
make bootstrap-dev
make bootstrap-operations
make bootstrap-staging
make bootstrap-production
```

Connect your repo to AWS CodeStar. (TODO: Add instructions).
