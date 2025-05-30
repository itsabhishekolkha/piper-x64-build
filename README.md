# Piper TTS Static Binary for macOS

A GitHub Actions workflow that automatically builds a standalone Piper TTS binary for macOS Intel systems, complete with voice models and dependencies bundled.

## What is This?

This repository contains a GitHub Actions workflow that creates a self-contained, portable Piper TTS (Text-to-Speech) application for macOS. The resulting binary requires no additional installation or dependencies - just download and run.

## Features

- **Standalone Binary**: No Python installation required
- **Pre-bundled Voice Model**: Includes high-quality English voice (en_US-lessac-medium)
- **Zero Dependencies**: All required libraries bundled into the executable
- **Intel Mac Compatible**: Built specifically for Intel-based Macs (macOS 13+)
- **Command-line Interface**: Simple terminal-based usage

## Quick Start

### Option 1: Download Pre-built Binary

1. Go to the [Actions](../../actions) tab
2. Find the latest successful "Build Intel Binary for Testing" workflow run
3. Download either:
   - `piper-intel-bundle.tar.gz` (complete folder structure)
   - `piper-intel-executable` (standalone binary only)

### Option 2: Build Your Own

1. Fork this repository
2. Go to the Actions tab in your fork
3. Click "Build Intel Binary for Testing (Terminal Method)"
4. Click "Run workflow"
5. Wait for the build to complete (usually 3-5 minutes)
6. Download the artifacts

## Usage

### Using the Complete Bundle

```bash
# Extract the bundle
tar -xzf piper-intel-bundle.tar.gz
cd piper

# Basic usage
echo "Hello, world!" | ./bin/piper --model voices/en_US-lessac-medium.onnx --output_file output.wav

# Play the audio (macOS)
afplay output.wav
```

### Using Just the Executable

```bash
# Make executable
chmod +x piper

# You'll need to download voice models separately
curl -L -O https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
curl -L -O https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json

# Generate speech
echo "Your text here" | ./piper --model en_US-lessac-medium.onnx --output_file speech.wav
```

## Command Line Options

```
--model MODEL_PATH     Path to the .onnx voice model file (required)
--output_file FILE     Output WAV file path (required)
```

Input text is read from stdin.

## Voice Models

The default bundle includes the `en_US-lessac-medium` voice model, which provides:
- High-quality English speech synthesis
- Medium-sized model (good balance of quality vs. size)
- Natural-sounding American English accent

### Adding More Voices

You can download additional voice models from [Piper Voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices):

```bash
# Example: Download a different English voice
curl -L -O https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx
curl -L -O https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx.json
```

## Technical Details

### Build Process

The GitHub Actions workflow:

1. Sets up Python 3.12 on macOS Intel runner
2. Creates a virtual environment
3. Installs Piper TTS (version 1.2.0)
4. Downloads voice models from Hugging Face
5. Creates a simple command-line wrapper script
6. Uses PyInstaller to create a standalone executable
7. Bundles everything into a portable folder structure
8. Creates compressed archives for distribution

### File Structure

```
piper/
├── bin/
│   └── piper              # Standalone executable
├── voices/
│   ├── en_US-lessac-medium.onnx
│   └── en_US-lessac-medium.onnx.json
└── lib/                   # Optional libraries (backup)
```

### System Requirements

- macOS 13 or later
- Intel-based Mac (x86_64 architecture)
- No additional software required

## Examples

### Basic Text-to-Speech

```bash
echo "Welcome to Piper TTS!" | ./bin/piper --model voices/en_US-lessac-medium.onnx --output_file welcome.wav
```

### Reading from File

```bash
cat my_text.txt | ./bin/piper --model voices/en_US-lessac-medium.onnx --output_file reading.wav
```

### Interactive Usage

```bash
# Type your text, then press Ctrl+D to finish
./bin/piper --model voices/en_US-lessac-medium.onnx --output_file interactive.wav
```

## Troubleshooting

### Permission Denied
```bash
chmod +x ./bin/piper
```

### "Cannot verify developer" on macOS
```bash
sudo xattr -rd com.apple.quarantine ./bin/piper
```

### Voice Model Not Found
Ensure the model path is correct and both `.onnx` and `.onnx.json` files are present.

## About Piper TTS

Piper is a fast, local neural text-to-speech system developed by Rhasspy. It's designed to be:
- Fast and efficient
- High quality
- Multilingual
- Privacy-focused (runs entirely offline)

Original project: [rhasspy/piper](https://github.com/rhasspy/piper)

## License

This build workflow is provided as-is. Piper TTS itself is licensed under the MIT License. Voice models may have their own licensing terms.

## Contributing

Feel free to:
- Report issues with the build process
- Suggest improvements to the workflow
- Add support for ARM64 Macs
- Submit pull requests

## Changelog

### Latest Build
- Python 3.12 support
- Improved PyInstaller configuration
- Automatic espeak-ng-data bundling
- Compressed bundle distribution
- Complete folder structure with voice models
