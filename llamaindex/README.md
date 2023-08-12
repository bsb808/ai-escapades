# Your Data, Their AI: Using Llama index to provide a LLM interface to custom/private information.

Code example to go along with the blog post: TBD

##

## Install in a virtual environment


1. If you don't have the `venv` package, install:

   ```bash
   sudo apt install python3.10-venv
   ```

2. Clone this repository.

   ```bash
   git clone https://github.com/bsb808/ai-escapades.git
   ```

3. Navigate into the project directory:

   ```bash
   cd ai-escapades/llamaindex
   ```
4. Create and activate a new virtual environment:

   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

Install Llama Index:


pip install llama-index

5. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

# Get some data

For starter example - put the paul gram essay in the data directory

# Setup your API key


Make sure not to share - put links to news articles

   ```bash
   cp .env.example .env
   ```
# Load the .env variables and set API key.
load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")
