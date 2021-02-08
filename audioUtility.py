# Import the base64 encoding library.
import base64

# Pass the audio data to an encoding function.
def audioToString(audio_path):
    return base64.b64encode(open(audio_path, "rb").read())

def stringToAudio(audioString, output_audio_path):
    wav_file = open(output_audio_path, "wb")
    decode_string = base64.b64decode(audioString)
    wav_file.write(decode_string)

if __name__ == "__main__":
    input_audio_path = './example.mp3'
    output_audio_path = './example_op.mp3'
    result_string = audioToString(input_audio_path)
    print("CONVERTED AUDIO TO STRING")
    stringToAudio(result_string, output_audio_path)
    print("CONVERTED STRING TO AUDIO")