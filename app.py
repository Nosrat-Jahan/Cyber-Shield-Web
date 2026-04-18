"""
=============================================================================
SOURCE   : Cyber_Shield_Web_Engine.py
VERSION  : 6.6.6 [Stable]
DEV      : Nosrat Jahan
ACADEMIC : BSc in CSE
-----------------------------------------------------------------------------
DESCRIPTION: Flask-based security module with Eye-toggle for visibility.
Features a responsive web UI with real-time entropy calculation.
=============================================================================
"""

from flask import Flask, render_template_string, request
import re
import os

app = Flask(__name__)

# UI Template - Designed for clarity and responsiveness
UI_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber-Shield Web v6.6.6</title>
    <style>
        body { background-color: #1e272e; color: #d2dae2; font-family: 'Consolas', 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
        .wrapper { background-color: #2f3640; padding: 45px; border-radius: 8px; box-shadow: 0 20px 50px rgba(0,0,0,0.7); width: 100%; max-width: 500px; border-top: 5px solid #05c46b; transition: all 0.3s ease; }
        h2 { color: #05c46b; text-align: center; margin-bottom: 35px; letter-spacing: 2px; text-transform: uppercase; font-weight: bold; }
        
        .input-group { position: relative; width: 100%; margin-bottom: 25px; }
        input[type="password"], input[type="text"] { width: 100%; padding: 15px; padding-right: 50px; border: 1px solid #485460; border-radius: 4px; background: #1e272e; color: #fff; box-sizing: border-box; outline: none; transition: 0.4s; font-size: 16px; }
        input:focus { border-color: #05c46b; box-shadow: 0 0 10px rgba(5, 196, 107, 0.2); }
        
        .toggle-eye { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); cursor: pointer; color: #808e9b; font-size: 20px; user-select: none; }
        .toggle-eye:hover { color: #05c46b; }

        button { background-color: #05c46b; color: #fff; border: none; padding: 15px; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; font-size: 15px; transition: 0.3s; text-transform: uppercase; }
        button:hover { background-color: #0be881; transform: translateY(-1px); }
        
        .report-box { margin-top: 35px; padding: 20px; background: #1e272e; border-left: 4px solid; animation: fadeIn 0.5s ease; }
        .footer-info { margin-top: 40px; text-align: center; font-size: 12px; color: #05c46b; border-top: 1px solid #3d4e5f; padding-top: 20px; cursor: pointer; font-weight: bold; letter-spacing: 1px; }
        .footer-info:hover { color: #0be881; text-decoration: underline; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="wrapper">
        <h2>Cyber-Shield Engine</h2>
        <form method="POST">
            <div class="input-group">
                <input type="password" name="cred_input" id="password_input" placeholder="Input Credential for Analysis..." autocomplete="off" required>
                <span class="toggle-eye" id="toggle_eye" onclick="togglePassword()">👁</span>
            </div>
            <button type="submit">Initialize Security Scan</button>
        </form>

        {% if analysis_done %}
        <div class="report-box" style="border-color: {{ color }};">
            <div style="color: {{ color }}; font-weight: bold; font-size: 16px;">STATUS: {{ status }}</div>
            <div style="margin-top: 15px; font-size: 13px; line-height: 1.6;">
                {% for log in logs %}
                    <div style="color: #ff3f34;">[!] {{ log }}</div>
                {% endfor %}
                {% if not logs %}
                    <div style="color: #05c46b;">[SYNC] Integrity: HIGH. Brute-force resistance optimal.</div>
                {% endif %}
            </div>
        </div>
        {% endif %}

        <div class="footer-info" onclick="alert('SYSTEM METADATA\\n-------------------\\nCore Version: 6.6.6\\nArchitect: Nosrat Jahan\\nAcademic: BSc in CSE\\nAlgorithm: Multi-layered Entropy Check')">
            [ VIEW SYSTEM METADATA ]
        </div>
        
        <div style="text-align: center; margin-top: 15px; font-size: 10px; color: #485460;">
            v6.6.6 | Engineered by Nosrat Jahan | 2026
        </div>
    </div>

    <script>
        function togglePassword() {
            const passInput = document.getElementById("password_input");
            const eyeIcon = document.getElementById("toggle_eye");
            if (passInput.type === "password") {
                passInput.type = "text";
                eyeIcon.style.color = "#05c46b";
            } else {
                passInput.type = "password";
                eyeIcon.style.color = "#808e9b";
            }
        }
    </script>
</body>
</html>
"""

def evaluate_entropy(token):
    score = 0
    logs = []
    
    # Validation Logic Matrix
    if len(token) >= 12: score += 2
    elif len(token) >= 8: score += 1
    else: logs.append("Security Gap: Insufficient character length.")
    
    if any(c.isupper() for c in token) and any(c.islower() for c in token): score += 1
    else: logs.append("Metric Fail: Mixed-case diversity missing.")
    
    if any(c.isdigit() for c in token): score += 1
    else: logs.append("Metric Fail: Numeric digit presence missing.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", token): score += 1
    else: logs.append("Metric Fail: Special character entropy low.")

    if score >= 5: return "ELITE PROTECTION", "#05c46b", logs
    elif score >= 3: return "MODERATE RISK", "#ffdd59", logs
    else: return "CRITICAL VULNERABILITY", "#ff3f34", logs

@app.route("/", methods=["GET", "POST"])
def main_portal():
    if request.method == "POST":
        cred = request.form.get("cred_input")
        status, color, logs = evaluate_entropy(cred)
        return render_template_string(UI_LAYOUT, analysis_done=True, status=status, color=color, logs=logs)
    return render_template_string(UI_LAYOUT, analysis_done=False)

if __name__ == "__main__":
    # Internal Network Configuration
    host_addr = "127.0.0.1"
    port_no = 5000
    
    print("\n" + "="*60)
    print("  CYBER-SHIELD WEB ENGINE v6.6.6 [STABLE RELEASE]")
    print(f"  Access Link: http://{host_addr}:{port_no}")
    print("  Status: local_server_initialized...")
    print("="*60 + "\n")
    
    app.run(host=host_addr, port=port_no, debug=False)
