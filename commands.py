import subprocess

def execute_command(command):
   
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except subprocess.TimeoutExpired:
        return "⏳ Error: Command timed out."
    except Exception as e:
        return f"❌ Error executing command: {str(e)}"
