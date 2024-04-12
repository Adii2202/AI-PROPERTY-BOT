# Real Estate Finance Crew

## Setting Up the Environment

1. **Create Conda Environment**:
    ```bash
    conda create -n crew python=3.11
    ```

2. **Activate Conda Environment**:
    ```bash
    conda activate crew
    ```

3. **Get Ollama and Openhermes Model**:
    ```bash
    ollama pull openhermes
    ```

4. **Install Requirements**:
    ```bash
    pip install 'crewai[tools]'
    pip install -r requirements.txt
    ```

## Running the Financial Expert Bot

1. **Get Serper API Key**:
    - Obtain your Serper API key from [Serper Dev](https://serper.dev/api-key).

2. **Run the Financial Expert Bot**:
    ```bash
    ollama run openhermes
    ```

## Additional Resources

- For more information on using Crew AI, refer to the [Crew AI Documentation](https://docs.crewai.com/).
