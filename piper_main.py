import sys
from piper import PiperVoice
import wave
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    # Read text from stdin
    text = sys.stdin.read().strip()
    if not text:
        sys.exit(1)

    # Load voice
    voice = PiperVoice.load(args.model)

    # Synthesize
    with wave.open(args.output_file, "w") as wav_file:
        voice.synthesize(text, wav_file)

if __name__ == "__main__":
    main()
