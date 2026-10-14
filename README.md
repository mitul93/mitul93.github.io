# Personal GitHub Pages

This repository is used to develop and maintain a personal website and blog deployed with GitHub Pages.

## Project structure

```text
├── .github/              
│   └── workflows/     # Github workflows
│       └── hugo.yml   # Github pages pipeline
│
├── scripts/           # Scripts
│
├── deployment.yaml    # Github Pages deployment configuration
└── README.md
```

## Steps to Deploy

To deploy a new version of the website:

1. Update the `tag` in `deployment.yaml` to the desired release of `mitul93/my-website`.
2. Commit the change and merge it into `main`.
3. GitHub Actions automatically builds and deploys the specified version.