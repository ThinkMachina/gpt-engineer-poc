# GPT Engineer Proof of Concept (PoC)
This repository contains a proof of concept (PoC) for GPT Engineer, a powerful tool that uses AI to generate code based on your prompts.

# Setup
To set up the GPT Engineer for this PoC, follow these steps:

1. Clone the GPT Engineer repository:

```bash
git clone https://github.com/AntonOsika/gpt-engineer.git
```

2. Create a new directory for the PoC and copy the example project into it:

```bash
mkdir gpt-engineer-poc
cp gpt-engineer/projects/example/ gpt-engineer-poc/
```

3. Navigate to the PoC directory:

```bash
cd gpt-engineer-poc
```

4. Install GPT Engineer:

```bash
pip install gpt-engineer
```

5. Fill in your prompt in the `prompt` file.

6. Run GPT Engineer:

```bash
.venv/bin/gpt-engineer .
```

# Execution
To execute the code generated by GPT Engineer, follow these steps:

1. Navigate to the workspace directory:

```bash
cd workspace
```

2. Run the generated script:

```bash
bash run.sh
```

3. The API will be reachable at http://127.0.0.1:5000.

# Testing
To test the generated code, use Postman:

1. Open Postman.

2. Click on 'Import'.

3. Select the `todo_list_api.postman_collection.json` file to import the collection.

4. Run the requests in the imported collection to test the generated API.