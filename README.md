# Speech Analysis CLI Tool with Gemini API

A sophisticated command-line tool for analyzing political speeches using Google's Gemini API and advanced prompt engineering. This tool provides deep insights into speeches by examining context, themes, foreign policy stances, tone, and potential consequences.

## Features

- **Comprehensive Speech Analysis**: Breaks down speeches into multiple analytical components
- **Structured Output**: Returns analysis in well-organized JSON format using Pydantic models
- **Multi-dimensional Analysis**:
  - Speech context (domestic and international)
  - Key themes identification
  - Foreign policy stance analysis
  - Tone assessment
  - Ambiguity level evaluation
  - Short and long-term consequence prediction
  - Media reaction forecasting
- **Intelligent Context Analysis**: 
  - Keyword mention counting
  - Context window extraction
  - Historical reference lookup
  - Speaker biography integration
- **Unbiased Methodology**: Maintains consistent analytical rigor across all speech origins
- **Omission Detection**: Notes significant gaps in speech content for deeper insights

## Requirements

- Python 3.8+
- Google Gemini API key
- Required Python packages:
  - `google-genai`
  - `pydantic`
  - `requests`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Speech analysis CLI tool using Prompt engineering"
```

2. Install dependencies:
```bash
pip install google-genai pydantic requests
```

3. Set up your Google Gemini API key:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Usage

1. **Prepare your speech**: Place the speech text in `Speech.txt` in the project directory

2. **Run the analysis**:
```bash
python "Speech analysis - CLI Tool with Gemini API.py"
```

3. **View results**: The analysis will be saved to `Speech_analysis.txt` in JSON format

### Input Format

Create a `Speech.txt` file with the full transcript of the speech you want to analyze.

### Output Format

The tool generates a JSON file (`Speech_analysis.txt`) with the following structure:

```json
{
  "speech_context": {
    "domestic_context": "...",
    "international_context": "..."
  },
  "themes": [
    {
      "name": "...",
      "description": "..."
    }
  ],
  "foreign_policy_analysis": {
    "stance": "..."
  },
  "tone_analysis": {
    "tone": "..."
  },
  "ambiguity_assessment": {
    "ambiguity_level": "..."
  },
  "consequences": {
    "short_term_consequences": "...",
    "long_term_consequences": "..."
  },
  "media_reaction": {
    "media_reaction": "..."
  }
}
```

## Architecture

### Pydantic Models

The tool uses Pydantic models for structured analysis:

- **Speech**: Input model containing transcript, language, audience, and domain
- **SpeechContext**: Domestic and international context
- **Theme**: Identified themes with descriptions
- **ForeignPolicyAnalysis**: Foreign policy stance
- **ToneAnalysis**: Speech tone assessment
- **AmbiguityAssessment**: Ambiguity level evaluation
- **Consequences**: Short and long-term consequences
- **MediaReaction**: Predicted media reaction
- **SpeechAnalysis**: Main output model combining all analyses

### Analysis Methods

The tool employs several analytical techniques:

1. **count_mentions()**: Tracks keyword frequency in the speech
2. **context_around()**: Extracts surrounding context for specific phrases
3. **lookup_historical_references()**: Identifies historical allusions
4. **get_speaker_biography()**: Gathers speaker background information
5. **get_speaker_recent_speeches()**: Reviews speaker's recent addresses

### Analytical Principles

The analysis follows these key principles:

1. **Full Context Review**: Entire speech is read before analysis begins
2. **Background Integration**: Speaker history and recent activities inform analysis
3. **Detail-Oriented**: Dog whistles and subtle language patterns are examined
4. **Neutrality Maintained**: Same scrutiny applied regardless of speech origin
5. **Omission Awareness**: Significant absences in content are flagged
6. **Appropriate Skepticism**: Avoids over-interpretation of diplomatic boilerplate
7. **Uncertainty Acknowledgment**: Clearly states analytical limitations and doubts

## Example

The included example analyzes a diplomatic speech between India and Norway, identifying:
- Strategic partnership themes
- Arctic cooperation opportunities
- Climate and sustainability focus
- Geopolitical context (Ukraine, West Asia)
- Economic partnership targets

## Configuration

The tool uses the following configuration:

- **Model**: `gemini-3-flash-preview` (Google's fastest Gemini model)
- **Response Type**: Structured JSON output via response schema
- **Tool Use**: Enables the model to use analysis helper functions

## Customization

You can customize the analysis by:

1. Modifying the `PROMPT` variable to adjust analytical focus
2. Updating Pydantic models to capture additional analysis dimensions
3. Adding new analysis functions to the tools list
4. Changing the `MODEL` to use different Gemini versions

## Error Handling

The tool includes validation for:

- Empty speech input detection
- File I/O error handling
- API response validation
- JSON schema compliance

## Limitations

- Historical reference lookup currently uses placeholder data (can be enhanced with real APIs)
- Speaker biography data is placeholder-based (can connect to biographical databases)
- Speaker recent speeches are placeholder-based (can integrate with speech archives)

## Future Enhancements

- Integration with real historical fact databases
- Connection to speaker biographical APIs
- Real-time media source aggregation
- Comparison analysis across multiple speeches
- Interactive CLI interface with argument parsing
- Batch processing capabilities
- Custom analysis templates

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions and bug reports.


