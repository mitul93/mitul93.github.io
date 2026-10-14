#!/usr/bin/env python3

import sys

import yaml

def main():
    with open("deployment.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    tag = config["tag"]

    if not isinstance(tag, str) or not tag.strip():
        sys.exit("Error: 'tag' must be a non-empty string.")

    print(tag)

if __name__ == "__main__":
    main()