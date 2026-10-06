import subprocess

@app.route("/ping")
def ping():
    user_input = "example"
    result = subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout