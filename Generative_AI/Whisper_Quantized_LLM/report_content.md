# Report Content — Whisper + Quantized LLM Speech-to-Reasoning

## Student Information

- Name: Mehak Zahra
- Internship: Arch Technologies
- Domain: Generative AI
- Month: 2
- Task: 4
- Phone: 03322136800

Add the student's email address on the final report front page.

## Objective

The objective is to create an end-to-end speech-understanding pipeline. Whisper transcribes a spoken question, and a memory-efficient quantized language model interprets the transcription and generates a helpful response.

## Implementation

The user uploads a WAV, MP3 or M4A file to Google Colab. Faster-Whisper loads the Whisper small model on a Tesla T4 GPU and performs automatic speech recognition with voice-activity detection. The resulting transcription is inserted into a structured Llama 3.2 prompt. An Unsloth Dynamic 4-bit Llama 3.2 1B Instruct model generates a concise response. The transcription, response, model and GPU details are saved in a downloadable text file.

## Quantization

Dynamic 4-bit quantization reduces model-memory requirements and makes LLM inference practical on a limited cloud GPU while attempting to preserve important model parameters at suitable precision.

## Results

Insert actual screenshots showing the uploaded audio, detected language, Whisper transcription, quantized model loading, GPU-memory usage and final response. Mention the transcription quality observed for the recorded audio.

## Limitations

Transcription quality depends on microphone quality, noise, pronunciation and language. The small LLM can generate incomplete answers, so the output should be reviewed. Spoken input should not contain sensitive information.

## Conclusion

The project demonstrates the integration of automatic speech recognition and quantized language-model inference in a complete speech-to-response workflow.

## Tools

Google Colab, Tesla T4, Python, Faster-Whisper, Unsloth, Llama 3.2 and PyTorch.
