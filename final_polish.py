with open("IEEE_Conf.tex", "r", encoding="utf-8") as f:
    text = f.read()

old1 = r"""\section{Result Analysis and Discussion}

\subsection{Demographics and Travel Habits}"""

new1 = r"""\section{Result Analysis and Discussion}

\subsection{Survey Overview}

A primary survey titled ``Train Food Service Survey: Passenger Preferences and Feedback'' was conducted with 27 respondents to complement the literature review with empirical passenger data. To systematically break down the findings, this section evaluates the participant data across five core themes: Demographics and Travel Habits, Current Train Food Experience, Mobile Ordering Preferences, Food Waste and Sustainability, and Transparency and Trust. Crucially, the chart percentages are interpreted alongside their likely behavioral and operational causes, ensuring the findings support actionable design decisions rather than just descriptive reporting.

\subsection{Demographics and Travel Habits}"""

text = text.replace(old1, new1)

old2 = r"""According to Figure~\ref{fig:app}, 51.8\% of users (33.3\% ''Definitely yes'' and 18.5\% ''Probably yes'') intend to use a mobile app for train food."""
new2 = r"""According to Figure~\ref{fig:app}, 51.8\% of users (33.3\% ``Definitely yes'' and 18.5\% ``Probably yes'') intend to use a mobile app for train food."""
text = text.replace(old2, new2)

old3 = r"""The preceding survey analysis (Sections A through E) transitions the focus from merely reporting raw percentages to understanding the underlying behavioral causes."""
new3 = r"""The preceding survey analysis across these five themes transitions the focus from merely reporting raw percentages to understanding the underlying behavioral causes."""
text = text.replace(old3, new3)

with open("IEEE_Conf.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Formatting polished!")
