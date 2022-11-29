# modal-fullstack-example

Run a fullstack example app on [Modal](https://modal.com).

## Usage

A proof-of-concept, fullstack service, fullstack meaning frontend ui and backend api, that runs on [Modal](https://modal.com).

To get started, first clone this repo

```bash
git clone https://github.com/anthonycorletti/modal-fullstack-example.git
```

Then, follow the [contributing guide](./CONTRIBUTING.md) to install the app.

Once the app is installed, you can run it locally –

Install and build tailwindcss

```sh
./scripts/install-tailwind.sh
./scripts/build-tailwind.sh
```

Then, run the app

```sh
./scripts/run-uvicorn.sh
```

When you're ready to deploy to modal you can run

```sh
./scripts/modal-deploy.sh
```
