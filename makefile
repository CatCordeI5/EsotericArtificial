.PHONY: help install run clean

help:
	@echo "╔═══════════════════════════════════════╗"
	@echo "║       ESOTERIC ARTIFICIAL MAKEFILE    ║"
	@echo "╠═══════════════════════════════════════╣"
	@echo "║  make install  - Install dependencies ║"
	@echo "║  make run      - Start Lunoia CLI     ║"
	@echo "║  make clean    - Remove cache/files   ║"
	@echo "╚═══════════════════════════════════════╝"

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "Done! Ready to run."

run:
	@echo "Starting Lunoia v0.1 (EsoArtificial)..."
	python lunoia_cli.py

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf *.pyc
	rm -f memory.json
	@echo "Cleaned!"
