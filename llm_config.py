DEFAULT_LLM_MODELS = {
    'openai': 'gpt-4o-2024-08-06',
    'openrouter': 'openai/gpt-4o-2024-08-06',
    'vertex': 'google/gemini-3.1-pro-preview',
}


def get_default_llm_model(provider):
    try:
        return DEFAULT_LLM_MODELS[provider]
    except KeyError as e:
        raise ValueError(
            f'Unsupported provider: {provider}. Expected one of '
            f"{', '.join(DEFAULT_LLM_MODELS.keys())}.") from e
