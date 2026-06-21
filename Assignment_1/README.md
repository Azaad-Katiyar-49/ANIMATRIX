# Manim GenAI Assignment: Code Generation and Critical Review

## Repository Overview
This project documents the process of using the Google Generative AI (Gemini) API to automate the creation of mathematical animations using the Manim library. The main objective is to utilize an LLM to generate animation scripts, execute the resulting code locally to identify visual or logical errors, implement necessary fixes, and evaluate the model's output.

The assignment targets two specific mathematical concepts:
1. **Pythagorean Theorem Visualization**: An animation demonstrating a right-angled triangle, properly labeled sides, shaded squares attached to each edge to represent area equivalence, and the display of the algebraic formula $a^2+b^2=c^2$.
2. **Fourier Series Decomposition**: A coordinate-based animation showing the step-by-step synthesis of a square wave. This is done by adding individual sine wave harmonics ($n=1,3,5,7,9$) using distinct colors to show the cumulative wave updating over time.

---

## Project Structure
Files are organized into dedicated task folders to maintain modularity, rather than being placed directly in the root directory:

```text
manim-genai-assignment/
├── .gitignore                # Git ignore rules for Python environments
├── requirements.txt          # Required packages (manim, numpy, google-generativeai)
├── README.md                 # Setup instructions and critical analysis
├── task1_pythagoras/
│   ├── generate_scene.py     # Script containing the Gemini API call and prompt
│   └── pythagoras.py         # The corrected and refactored Manim animation code
└── task2_fourier/
    ├── generate_scene.py     # Script containing the Gemini API call and prompt
    └── fourier_series.py     # The corrected and refactored Manim animation code

Setup Instructions:
1. PrerequisitesBefore running the animation scripts, ensure your system has the following core utilities installed:Python: python >= 3.8FFmpeg: Required by Manim for media processing and rendering output video codecs. Ensure it is appended to your environment's system PATH variables.(Optional) LaTeX Distribution: (e.g., MiKTeX on Windows or MacTeX on macOS). Note that the finalized code versions in this repository have been fully refactored to use standard text arrays to bypass local system LaTeX crashes (WinError 2).2. InstallationClone the repository and install the dependencies inside a dedicated virtual environment:Bash# Clone the repository
git clone [https://github.com/YOUR_USERNAME/manim-genai-assignment.git](https://github.com/YOUR_USERNAME/manim-genai-assignment.git)
cd manim-genai-assignment

# Create and activate a virtual environment
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
3. Environment ConfigurationTo run the automated script generators, configure your Gemini API token as an environment variable in your terminal session.On Windows (PowerShell):PowerShell$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
On macOS/Linux:Bashexport GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
How to Run Each Manim SceneTo render the scenes with standard low quality (useful for rapid previewing and testing), execute the following commands inside your terminal:Rendering Task 1: Pythagorean TheoremBashmanim -pql task1_pythagoras/pythagoras.py PythagorasScene
Rendering Task 2: Fourier Series DecompositionBashmanim -pql task2_fourier/fourier_series.py FourierSeries
