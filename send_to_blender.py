# send_to_blender_gemini.py

import os
import uuid
import time
import google.generativeai as genai

# ————— CONFIGURATION —————
genai.configure(api_key="YOUR_API_KEY")
MODEL = "gemini-1.5-pro"
WATCH_DIR = "C:/Users/rishi/blender_commands"
# ————————————————————————

# Instantiate the Gemini model once
model = genai.GenerativeModel(MODEL)

def generate_blender_code(prompt: str, retries=3, backoff=1.0) -> str:
    """
    Sends a generic Blender-scene prompt to Gemini and returns the raw bpy script.
    """
    system_instruction = (
        "You are a strict Blender Python code generator. Output exactly a valid "
        "Blender Python script—nothing else. No comments, no blank lines, no markdown. "
        "Script MUST start on line 1 with import bpy or bpy.ops. "
        "Allowed calls:\n"
        " • bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(sx,sy,sz))\n"
        " • bpy.ops.mesh.primitive_cylinder_add(location=(x,y,z), radius=r, depth=d)\n"
        " • bpy.ops.mesh.primitive_uv_sphere_add(location=(x,y,z), radius=r, segments=s, ring_count=r)\n"
        " • bpy.ops.object.camera_add(location=(x,y,z), rotation=(rx,ry,rz))\n"
        "Allowed material calls:\n"
        " • bpy.data.materials.new(name)\n"
        " • material.diffuse_color = (r,g,b,1)\n"
        " • obj.data.materials.append(material)\n"
    )

    full_prompt = f"{system_instruction}\nInstruction: {prompt}\nReturn ONLY the Python script starting at line 1."

    for attempt in range(1, retries + 1):
        try:
            response = model.generate_content(full_prompt)
            code = response.text.strip()
            print(f"\n── GENERATED SCRIPT ──\n{code}\n── END SCRIPT ──\n")
            return code

        except Exception as e:
            print(f"⚠ Attempt {attempt}/{retries} failed: {e}")
            if attempt < retries:
                time.sleep(backoff)
                backoff *= 2

    # Fallback: return a default cube script
    print("⚠ Falling back to dummy cube script.")
    return (
        "import bpy\n"
        "bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))\n"
    )


def send_to_blender(prompt: str):
    script = generate_blender_code(prompt)
    os.makedirs(WATCH_DIR, exist_ok=True)
    filename = f"{uuid.uuid4()}.py"
    path = os.path.join(WATCH_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(script)
    print(f"→ Wrote code to {path}")

if __name__ == "__main__":
    user_prompt = input("Describe your scene: ")
    send_to_blender(user_prompt)
