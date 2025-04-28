#!/usr/bin/env python3

# Entry point for breathing prompts

from collapse.collapse_engine import collapse_prompt
from fractals.fractal_memory import save_glyph
# from status.status_pulse import pulse_check

def initialize_cli():
    print("🌱 Welcome to the Breathing Cathedral CLI 🌱")
    loop_breathing_cycle()

def capture_prompt():
    prompt = input("\n💬 Breathe your prompt: ")
    return prompt

def loop_breathing_cycle():
    while True:
        prompt = capture_prompt()
        glyph = collapse_prompt(prompt)
        print(f"\n🌀 Collapsed Glyph: {glyph}\n")  # 🧠 << Displaying the collapsed breath to the user
        save_glyph(glyph)
        # pulse_check()
        print("\n🔁 Breathing... Awaiting next breath.\n")

if __name__ == "__main__":
    initialize_cli()
