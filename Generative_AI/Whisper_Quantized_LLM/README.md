# Generative AI Month 2 — Task 4

## Whisper + Quantized LLM Speech-to-Reasoning

This Google Colab project converts an uploaded audio question into text with Whisper and sends the transcription to an Unsloth Dynamic 4-bit Llama model for a concise, useful response.

### Files

- `GenAI_Task4_Whisper_Quantized_LLM.ipynb` — ready-to-run Colab notebook
- `audio/README.txt` — recording and upload instructions
- `sample_output.txt` — expected output format
- `report_content.md` — internship-report material
- `requirements.txt` — notebook dependencies

### How to Run

1. Open https://colab.research.google.com/.
2. Select `File → Upload notebook`.
3. Upload `GenAI_Task4_Whisper_Quantized_LLM.ipynb`.
4. Select `Runtime → Change runtime type → T4 GPU`.
5. Run cells in order.
6. When requested, upload a short `.wav`, `.mp3` or `.m4a` audio recording.
7. Verify the Whisper transcription.
8. Run the quantized LLM cells and capture the final response.
9. Download the automatically created `speech_to_reasoning_output.txt`.

### Suggested Audio Question

Record clearly:

`What are three practical ways a student can manage study time effectively?`

Avoid including private or sensitive information in the recording.

### Report Screenshots

- Tesla T4 output
- Package/GPU verification
- Uploaded audio filename
- Detected language and Whisper transcription
- Dynamic 4-bit model name and GPU memory
- Final LLM response
- Downloaded output file
