# [TBD] Once the code editor works in the texting page, move it here
import streamlit as st
import subprocess
from streamlit_ace import st_ace


def code_editor(height="300px", sample_code = "", editor_label = "",min_lines = 20):
    with st.container():
        content = st_ace(
                    height=height,
                    value= sample_code,
                    placeholder="Put the code here and click 'APPLY' to run",
                    language= "python",
                    theme="github",
                    font_size= 15,
                    tab_size=4,
                    show_gutter=True, # line number
                    min_lines=min_lines,
                    key=editor_label, #lable of the code editor

                    # show_print_margin=c2.checkbox("Show print margin", value=False),
                    # wrap=c2.checkbox("Wrap enabled", value=False),
                    # auto_update=c2.checkbox("Auto update", value=False),
                    # readonly=c2.checkbox("Read-only", value=False),
                    # keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),


                )

        if content:
            with open("./webpages/input_code.py", "w") as f:
                f.write(content)

            try: 
                result = subprocess.run(
                            ["python", "./webpages/input_code.py"],  # use python or python3 command to execute file
                            capture_output=True,            # Capture both stdout and stderr
                            text=True,                      # Ensure the output is returned as a string
                            timeout=10                      # Timeout after 10 seconds
                        )
                # Check if the process encountered an error (non-zero exit code)
                if result.returncode != 0:
                    st.error("Error:\t"+ result.stderr)            # Print the error details from code.py
                else:
                    st.success("**Code Output:**")
                    st.text(result.stdout)            # Print the normal output if no errors
            
            except subprocess.TimeoutExpired:
                # Handle case where the process runs for too long
                st.exception("The code took too long to execute and was terminated.")
        st.divider()    
        
