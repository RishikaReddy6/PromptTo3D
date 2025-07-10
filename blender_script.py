# blender_folder_watcher.py
import bpy, os
from pathlib import Path

WATCH_DIR = Path("C:/Users/rishi/blender_commands")
WATCH_DIR.mkdir(parents=True, exist_ok=True)

def process_files():
    for file in WATCH_DIR.glob("*.py"):
        try:
            code = file.read_text(encoding="utf-8")
            exec(compile(code, str(file), 'exec'), {'bpy': bpy})
            print(f"✅ Ran {file.name}")
        except Exception as e:
            print(f"❌ {file.name} failed: {e}")
        file.unlink()

def watch_folder():
    process_files()
    return 1.0  # every 1s

bpy.app.timers.register(watch_folder)
print(f"👀 Watching {WATCH_DIR}")
