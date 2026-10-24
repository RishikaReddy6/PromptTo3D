## **PromptTo3D**

**PromptTo3D** is an AI-powered tool that lets you generate 3D models in Blender using natural language prompts. It connects a local LLM like Gemini with Blender, allowing users to script Blender scenes just by describing them.

## 🚀 How It Works

This project runs with two main components:

### 1. `send_to_blender.py`

This Python script handles user interaction:

* Takes a prompt (like “create a stylized cupcake with frosting and a cherry on top”)
* Sends it to the LLM (Gemini)
* Retrieves the generated Blender Python script
* Automatically passes the script to Blender via the MCP server

### 2. `blender_script.py`

This script is run **inside Blender**. It:

* Sets up a local MCP server within Blender
* Waits for incoming model-generation scripts
* Executes them in Blender to render the scene

## 🧰 Requirements

* Blender (with MCP setup)
* Python 3
* Access to Gemini or any compatible LLM
* `requests`, `json`, and other standard Python libraries

## 📦 Setup & Run

1. Open `blender_script.py` in Blender's scripting tab and **run** it to start the MCP server.
2. From your terminal, run `send_to_blender.py` and enter your prompt.
3. Watch your idea take shape in Blender!

## 📁 Folder Structure

```
.
├── send_to_blender.py      # Main prompt handler and script sender
└── blender_script.py       # Blender-side server to receive and run model scripts
```

## 🌟 Features

* LLM-powered 3D generation
* Custom prompt handling
* Blender automation using MCP
* Rapid prototyping of simple models

## 🧪 Example Prompts

* “Model a glass of water with a transparent glass and blue water inside.”
* “Create a realistic burger with bun, patty, cheese, and lettuce.” lol
