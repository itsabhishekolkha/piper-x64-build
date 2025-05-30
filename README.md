# Piper TTS - x64 Static Binaries for Intel Macs & Windows

<div align="center">

[![x64](https://img.shields.io/badge/x64-Intel%20Compatible-blue?style=for-the-badge&logo=intel)](https://github.com/yourusername/piper-x64)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/yourusername/piper-x64?style=for-the-badge)](https://github.com/yourusername/piper-x64/releases)

**High-quality, fast text-to-speech for Intel-based systems**

[Download](#download) • [Quick Start](#quick-start) • [Build Methods](#build-methods) • [⭐ Star Repository](#support-this-project) • [Support](#support-this-project)

</div>

---

## About

Piper is a fast, local neural text-to-speech system that produces high-quality synthetic speech. This repository provides pre-built x64 static binaries specifically optimized for Intel-based systems including Intel Macs, Windows, and Linux.

### Key Features

- **x64 Performance** - Fully optimized for Intel x86-64 architecture
- **Cross-Platform** - Works on Intel Macs, Windows, and Linux
- **Self-Contained Executable** - No Python installation or dependencies required
- **High-Quality Voice Synthesis** - Neural network-based text-to-speech
- **Lightweight & Fast** - Minimal system resources required
- **Command-Line Interface** - Simple integration into scripts and workflows

## Download

### Latest Release

Download the latest pre-built binaries from the [Releases](https://github.com/yourusername/piper-x64/releases) page.

Available downloads:
- `piper-x64-bundle.tar.gz` - Complete bundle with voice models (Terminal Method build)
- `piper-x64-alternative-bundle.tar.gz` - Alternative build with community wheels
- Standalone executables for both build methods

### System Requirements

**macOS (Intel):**
- macOS 10.14 (Mojave) or later
- Intel-based Mac
- ~50MB free disk space

**Windows:**
- Windows 10 or later
- x64 processor
- ~50MB free disk space

**Linux:**
- Most modern x64 Linux distributions
- GLIBC 2.17 or later
- ~50MB free disk space

## Quick Start

### Installation

1. Download the bundle from the releases page
2. Extract the archive:
   
   **macOS/Linux:**
   ```bash
   tar -xzf piper-x64-bundle.tar.gz
   ```
   
   **Windows:**
   ```cmd
   tar -xzf piper-x64-bundle.tar.gz
   # or use your preferred extraction tool
   ```

3. Navigate to the extracted folder:
   ```bash
   cd piper
   ```

### Basic Usage

Generate speech from text:

**macOS/Linux:**
```bash
echo "Hello, this is Piper TTS running on x64!" | ./bin/piper --model voices/en_US-lessac-medium.onnx --output_file output.wav
```

**Windows:**
```cmd
echo Hello, this is Piper TTS running on x64! | .\bin\piper.exe --model voices\en_US-lessac-medium.onnx --output_file output.wav
```

Generate speech from a text file:

**macOS/Linux:**
```bash
cat your_text.txt | ./bin/piper --model voices/en_US-lessac-medium.onnx --output_file speech.wav
```

**Windows:**
```cmd
type your_text.txt | .\bin\piper.exe --model voices\en_US-lessac-medium.onnx --output_file speech.wav
```

### Command Line Options

```bash
./bin/piper --model <path_to_model> --output_file <output.wav>
```

- `--model` - Path to the voice model (.onnx file)
- `--output_file` - Output WAV file path

## Build Methods

This project provides two different build approaches, each with specific advantages:

### Method 1: Terminal Method (Recommended)
- **Build File**: Uses the primary GitHub Actions workflow
- **Approach**: Installs piper-tts with `--no-deps` flag and manually installs dependencies
- **Advantages**: More reliable dependency resolution across platforms
- **Output**: `piper-x64-bundle.tar.gz`

### Method 2: Community Wheels Method
- **Build File**: Uses the alternative GitHub Actions workflow
- **Approach**: Leverages community wheels and includes system dependencies
- **Advantages**: Better compatibility with community packages
- **Output**: `piper-x64-alternative-bundle.tar.gz`

Both methods produce fully functional x64 binaries compatible with Intel-based systems. Choose the one that works best for your platform and use case.

## Voice Models

The binaries come with the `en_US-lessac-medium` voice model included. Additional voice models can be downloaded from the [Piper Voices repository](https://huggingface.co/rhasspy/piper-voices).

### Adding New Voices

1. Download voice files (.onnx and .onnx.json) from the Piper Voices collection
2. Place them in the `voices/` directory
3. Use the new model with the `--model` parameter

## Development

### Building from Source

The build process is automated using GitHub Actions. The workflows handle:

- Setting up Python 3.12 environment
- Installing dependencies with x64 compatibility
- Downloading voice models
- Creating PyInstaller executables
- Packaging final bundles for multiple platforms

To trigger a build:
1. Fork this repository
2. Go to Actions tab
3. Run "Build x64 Binary for Testing (Terminal Method)" or "Build x64 Binary (Alternative Method)"

### Technical Details

- **Python Version**: 3.12
- **Build Tool**: PyInstaller with `--onefile` flag
- **Dependencies**: numpy, onnxruntime, piper-tts
- **Voice Model**: Lessac medium quality English (US)
- **Architecture**: x86-64 compatible

## Platform-Specific Notes

### Intel Macs
- Full compatibility with Intel-based MacBooks and iMacs
- No Rosetta translation required
- Native x64 performance

### Windows
- Compatible with Windows 10 and later
- May require Visual C++ Redistributable (usually pre-installed)
- Windows Defender may flag the executable initially (false positive)

### Linux
- Tested on Ubuntu, CentOS, and Debian-based distributions
- May require `libc6` and other common libraries
- Should work on most modern x64 Linux systems

## Troubleshooting

### Common Issues

**Binary won't run on macOS**: Ensure you have the necessary permissions:
```bash
chmod +x ./bin/piper
```

**Windows security warning**: Right-click the executable and select "Run anyway" or add an exception to Windows Defender.

**Linux dependency issues**: Install common libraries:
```bash
sudo apt-get update && sudo apt-get install libc6 libstdc++6
```

**Model not found**: Verify the model path is correct and the .onnx file exists in the voices directory.

**Audio output issues**: Check that the output directory is writable and you have sufficient disk space.

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

**⭐ Love this project? Give it a star on GitHub!** Your star helps others discover these x64 builds and motivates continued development.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

The Piper TTS engine is developed by Rhasspy and is also under the MIT License.

## Support This Project

If you find this project helpful, consider supporting its development:

<div align="center">

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/yourusername)
[![Star on GitHub](https://img.shields.io/badge/⭐%20Star%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/yourusername/piper-x64)

Your support helps maintain and improve these x64 builds for the community. Consider starring the repository to show your appreciation!

</div>

---

## Acknowledgments

- [Piper TTS](https://github.com/rhasspy/piper) - The original Piper text-to-speech system
- [Rhasspy](https://github.com/rhasspy) - For developing the Piper TTS engine
- Intel and x64 community for testing and feedback

## Related Projects

- [Original Piper TTS](https://github.com/rhasspy/piper)
- [Piper Voices Collection](https://huggingface.co/rhasspy/piper-voices)
- [Home Assistant Piper Integration](https://www.home-assistant.io/integrations/piper/)
- [Piper ARM64 Binaries](https://github.com/yourusername/piper-arm64) - For Apple Silicon Macs

---

<div align="center">
<sub>Built with ❤️ for the x64 community</sub>
</div>
