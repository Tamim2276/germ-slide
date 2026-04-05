import re

with open("IEEE_Conf.tex", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(r"\subsection{A. Demographics and Travel Habits}", r"\subsection{Demographics and Travel Habits}")
text = text.replace(r"\subsection{B. Current Train Food Experience}", r"\subsection{Current Train Food Experience}")
text = text.replace(r"\subsection{C. Mobile Ordering Preferences}", r"\subsection{Mobile Ordering Preferences}")
text = text.replace(r"\subsection{D. Food Waste and Sustainability}", r"\subsection{Food Waste and Sustainability}")
text = text.replace(r"\subsection{E. Transparency and Trust}", r"\subsection{Transparency and Trust}")
text = text.replace(r"\subsection{F. Discussion}", r"\subsection{Discussion}")

with open("IEEE_Conf.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Subsections fixed.")
