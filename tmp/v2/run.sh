#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 {install|remove}"
  exit 1
fi

case "$1" in
    install)
        python3 -m venv venv
        source venv/bin/activate
        pip3 install -r req.txt
        echo "Virtual environment created. Please run 'source venv/bin/activate' to activate."
        ;;
    remove)
        rm -rf venv
        echo "Virtual environment removed."
        ;;
    *)
        echo "Opsi tidak valid. Gunakan install atau remove."
        exit 1
        ;;
esac