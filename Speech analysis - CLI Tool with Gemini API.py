import sys
from typing import Optional
import requests
import pydantic
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
import argparse
import os

# pydantic models for structured output:

class SpeechContext(pydantic.BaseModel):
    domestic_context: Optional[str] = Field(None, description="The domestic context of the speech (e.g., 'election campaign', 'policy announcement').")
    international_context: Optional[str] = Field(None, description="The international context of the speech (e.g., 'UN General Assembly', 'bilateral meeting').")

class Theme(pydantic.BaseModel):
    name: Optional[str] = Field(None, description="The name of the theme.")
    description: Optional[str] = Field(None, description="A brief description of the theme.")

class ForeignPolicyAnalysis(pydantic.BaseModel):
    stance: Optional[str] = Field(None, description="The foreign policy stance of the speaker (e.g., 'pro-Western', 'pro-Russian', 'neutral', 'none')")

class ToneAnalysis(pydantic.BaseModel):
    tone: Optional[str] = Field(None, description="The tone of the speech (e.g., 'positive', 'negative', 'neutral').")  

class AmbiguityAssessment(pydantic.BaseModel):
    ambiguity_level: Optional[str] = Field(None, description="The level of ambiguity in the speech (e.g., 'low', 'medium', 'high')")

class Consequences(pydantic.BaseModel):
    long_term_consequences: Optional[str] = Field(None, description="The potential long-term consequences of the speech (e.g., 'increased tensions', 'improved relations', 'economic impact')")
    short_term_consequences: Optional[str] = Field(None, description="The potential short-term consequences of the speech (e.g., 'immediate diplomatic response', 'market reaction', 'public opinion shift')")

class MediaReaction(pydantic.BaseModel):
    media_reaction: Optional[str] = Field(None, description="The potential media reaction to the speech (e.g., 'positive coverage', 'negative coverage', 'mixed coverage')")

class Speech(pydantic.BaseModel):
    #Basic Speech Information:
    transcript: str = Field(..., description="The transcript of the speech to be analyzed.")
    language: str = Field(..., description="The language of the speech (e.g., 'en' for English).")
    audience: Optional[str] = Field(None, description="The intended audience of the speech (e.g., 'general public', 'specific group', 'international community')")
    domain: Optional[str] = Field(None, description="The domain or context of the speech (e.g., 'political', 'economic', 'social').")

class SpeechAnalysis(pydantic.BaseModel):
    #Main class for the structured output of the speech analysis:
    speech_context: Optional[list[SpeechContext]] = Field(None, description="The context of the speech.")
    themes: Optional[list[Theme]] = Field(None, description="The main themes of the speech.")
    foreign_policy_analysis: Optional[list[ForeignPolicyAnalysis]] = Field(None, description="The analysis of the speaker's foreign policy stance.")
    tone_analysis: Optional[list[ToneAnalysis]] = Field(None, description="The analysis of the tone of the speech.")
    ambiguity_assessment: Optional[list[AmbiguityAssessment]] = Field(None, description="The assessment of ambiguity in the speech.")
    consequences: Optional[list[Consequences]] = Field(None, description="The potential consequences of the speech.")
    media_reaction: Optional[list[MediaReaction]] = Field(None, description="The potential media reaction to the speech.")

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

1. Avoid over-reading. Bland diplomatic boilerplate may be ignored.
2. Write what might you be wrong about? If you are not sure about something, say so.
"""

# Model

MODEL = "gemini-3-flash-preview"

# Main function to analyze the speech:

def main():
    parser = argparse.ArgumentParser(description="Analyze a head of state speech using Gemini API.")
    parser.add_argument(
        "file_or_text",
        nargs="*",
        help="Path to the speech text file, or raw speech text tokens passed directly on the command line.")
    parser.add_argument("--url", help="URL of the speech transcript (optional).")
    args = parser.parse_args()

    if args.url:
        speech = requests.get(args.url).text
    elif args.file_or_text:
        if len(args.file_or_text) == 1 and os.path.exists(args.file_or_text[0]):
            with open(args.file_or_text[0], 'r') as f:
                speech = f.read()
        else:
            speech = " ".join(args.file_or_text)
    else:
        speech = sys.stdin.read()

    if not speech.strip():
        print("No speech provided.")
        return
    
    # Initialize Gemini API client:
    client = genai.Client()
    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT + "\n\n" + speech,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=SpeechAnalysis,
        ),
    )

    print(response.text)

# Calling main:

if __name__ == "__main__":
    main()
