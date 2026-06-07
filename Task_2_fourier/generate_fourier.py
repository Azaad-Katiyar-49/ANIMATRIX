import os
from google import genai

# Set up the Gemini API client
gemini_api_client = genai.Client()

# Formulate the prompt based on the assignment criteria
fourier_prompt = """
Please generate a fully functional Python script using the Manim Community library.
The objective is to create an animation that visually decomposes a square wave using the Fourier Series.

Specific constraints:
- Illustrate the step-by-step synthesis of a square wave by adding sine wave harmonics.
- Animate at least the first five terms of the series.
- Use a distinct color for every individual harmonic wave.
- Display the cumulative sum of the waves dynamically as the animation progresses.
- Include standard graph elements: coordinate axes, text labels, a tracker/legend, and a main title.

Output ONLY the raw Python code within a standard markdown code block. Do not add any conversational text or explanations.
"""

print("Requesting Manim code for Fourier Series (Task 2) from Gemini API...")

api_response = gemini_api_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=fourier_prompt,
)

save_destination = "task2_fourier/fourier_series.py"

# Extract the raw code from the markdown formatting block
returned_text = api_response.text
if "```python" in returned_text:
    final_script = returned_text.split("```python")[1].split("```")[0].strip()
elif "```" in returned_text:
    final_script = returned_text.split("```")[1].split("```")[0].strip()
else:
    final_script = returned_text.strip()

# Save the extracted Python code
with open(save_destination, "w", encoding="utf-8") as target_file:
    target_file.write(final_script)

print(f"Success! The generated scene has been saved to {save_destination}")
