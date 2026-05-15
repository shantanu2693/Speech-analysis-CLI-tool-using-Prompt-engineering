from dataclasses import Field
from typing import Optional
import Pydantic
from google import genai
import argparse
import os

# Pydantic models for structured output:

class context(Pydantic.BaseModel):
    domestic_context: Optional[str] = Field(None, description="The domestic context of the speech (e.g., 'election campaign', 'policy announcement').")
    international_context: Optional[str] = Field(None, description="The international context of the speech (e.g., 'UN General Assembly', 'bilateral meeting').")

class theme(Pydantic.BaseModel):
    name: Optional[str] = Field(None, description="The name of the theme.")
    description: Optional[str] = Field(None, description="A brief description of the theme.")

class foreign_policy_analysis(Pydantic.BaseModel):
    stance: Optional[str] = Field(None, description="The foreign policy stance of the speaker (e.g., 'pro-Western', 'pro-Russian', 'neutral', 'none')")

class tone_analysis(Pydantic.BaseModel):
    tone: Optional[str] = Field(None, description="The tone of the speech (e.g., 'positive', 'negative', 'neutral').")  

class ambiguity_assessment(Pydantic.BaseModel):
    ambiguity_level: Optional[str] = Field(None, description="The level of ambiguity in the speech (e.g., 'low', 'medium', 'high')")

class consequences (Pydantic.BaseModel):
    long_term_consequences: Optional[str] = Field(None, description="The potential long-term consequences of the speech (e.g., 'increased tensions', 'improved relations', 'economic impact')")
    short_term_consequences: Optional[str] = Field(None, description="The potential short-term consequences of the speech (e.g., 'immediate diplomatic response', 'market reaction', 'public opinion shift')")

class media_reaction(Pydantic.BaseModel):
    media_reaction: Optional[str] = Field(None, description="The potential media reaction to the speech (e.g., 'positive coverage', 'negative coverage', 'mixed coverage')")

class Speech(Pydantic.BaseModel):
    #Basic Speech Information:
    transcript: str = Field(..., description="The transcript of the speech to be analyzed.")
    language: str = Field(..., description="The language of the speech (e.g., 'en' for English).")
    audience: Optional[str] = Field(None, description="The intended audience of the speech (e.g., 'general public', 'specific group', 'international community')")
    domain: Optional[str] = Field(None, description="The domain or context of the speech (e.g., 'political', 'economic', 'social').")

class Speech_analysis(Pydantic.BaseModel):
    #Main class for the structured output of the speech analysis:
    context: list[context] = Field(None, description="The context of the speech.")
    themes: list[theme] = Field(None, description="The main themes of the speech.")
    foreign_policy_analysis: [foreign_policy_analysis] = Field(None, description="The analysis of the speaker's foreign policy stance.")
    tone_analysis: [tone_analysis] = Field(None, description="The analysis of the tone of the speech.")
    ambiguity_assessment: [ambiguity_assessment] = Field(None, description="The assessment of ambiguity in the speech.")
    consequences: [consequences] = Field(None, description="The potential consequences of the speech.")
    media_reaction: [media_reaction] = Field(None, description="The potential media reaction to the speech.")

# Tool to analyze speeches using Gemini API:

def count_mentions (speech: str, keywords: list[str]) -> dict[str, int]:
    # This function counts the mentions of specific keywords in the speech.
    mentions = {keyword: speech.lower().count(keyword.lower()) for keyword in keywords}
    return mentions

def context_around (phrase: str, speech: str, window_size: int = 5) -> list[str]:
    # This function extracts the context around a specific phrase in the speech.
    words = speech.split()
    contexts = []
    for i in range(len(words)):
        if words[i].lower() == phrase.lower():
            start = max(0, i - window_size)
            end = min(len(words), i + window_size + 1)
            contexts.append(" ".join(words[start:end]))
    return contexts

def lookup_historical_references(speech: str) -> list[str]:
    # This function would ideally look up historical references in the speech using a knowledge base or API.
    # For demonstration purposes, we will return a hardcoded list of historical references.
    return [
        "Historical reference 1",
        "Historical reference 2",
        "Historical reference 3"
    ]

def get_speaker_biography(speaker_name: str) -> str:
    # This function would ideally fetch the biography of the speaker from a database or API.
    # For demonstration purposes, we will return a hardcoded biography.
    return f"{speaker_name} is a prominent political figure known for their influential speeches and policies."

def get_speaker_recent_speeches(speaker_name: str) -> list[str]:
    # This function would ideally fetch recent speeches of the speaker from a database or API.
    # For demonstration purposes, we will return a hardcoded list of speeches.
    return [
        "Speech 1 transcript...",
        "Speech 2 transcript...",
        "Speech 3 transcript..."
    ]

# Prompt

PROMPT = """You analyze head of state speeches by breaking down the speech into several components. 
Your role is a political analyst who is trained in international relations and political communication. 

METHOD:

1. Read the full transcript of the speech before analyzing.
2. Use get_speaker_recent_speeches and get_speaker_biography to build context about the speaker and their recent activities.
3. Use context_around, count_mentions and lookup_historical_references to analyze dog whistles.
4. Maintain neutrality. The same scrutiny applied to Biden's speech should be applied to Putin's speech, and vice versa. 
5. Note Omissions. If a US leader omits talking about immigration, for example, that is a significant omission and should be noted in the analysis.


DISCIPLINE:

1. Avoid over-reading. Not every phrase is coded. Not every audience shift is strategic. Bland diplomatic boilerplate is sometimes just boilerplate.
2. Write analyst_caveats genuinely. What might you be wrong about? What context would change the reading?
"""

# main function to analyze the speech:

def main():
# calling main:
