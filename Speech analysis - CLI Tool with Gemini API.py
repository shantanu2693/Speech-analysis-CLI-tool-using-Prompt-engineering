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

class ambiguity_and_impact_assessment(Pydantic.BaseModel):
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
    context: Optional[context] = Field(None, description="The context of the speech.")
    themes: Optional[list[theme]] = Field(None, description="The main themes of the speech.")
    foreign_policy_analysis: Optional[foreign_policy_analysis] = Field(None, description="The analysis of the speaker's foreign policy stance.")
    tone_analysis: Optional[tone_analysis] = Field(None, description="The analysis of the tone of the speech.")
    ambiguity_and_impact_assessment: Optional[ambiguity_and_impact_assessment] = Field(None, description="The assessment of ambiguity and potential impact of the speech.")
    consequences: Optional[consequences] = Field(None, description="The potential consequences of the speech.")
    media_reaction: Optional[media_reaction] = Field(None, description="The potential media reaction to the speech.")

# Tool to analyze speeches using Gemini API:

# main function to analyze the speech:

# calling main:
