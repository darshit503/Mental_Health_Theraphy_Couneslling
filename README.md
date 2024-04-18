# Mental Health Text Generation

![image](https://github.com/darshit503/Mental_Health_Theraphy_Couneslling/assets/91828073/97ef94ef-f943-41d5-bbeb-37f91df0d171)


## Description
This project is a Streamlit app that generates text based on mental health topics. It utilizes a language model to generate coherent and relevant text related to mental health. The Model used here is a Fine-Tuned Quantized model with 4 Bits of Precision. The Base  model is Open-Orca Mistral Model which is used for Text Generation and other tasks. This Fine Tuning and Quantization is done using Google Colab Notebook and further pushed to Hugging Face Repositories. This Project requires Ollama Software to run the Model and a good Computation Power GPU (RTX 30xx, RTX40xx, GTX 16xx, GTX 17xx) which helps in running the File and Project Smoothly. 

## Features
- Text generation based on mental health topics
- 4-bit precision model for faster inference
- Customizable text length and output format
- User-friendly interface with Streamlit

## Installation & Implementation
1. Clone the repository: `git clone https://github.com/your-username/mental-health-text-generation.git`
2. Run the Colab Notebook- Fine_Tuning_Quantized.ipynb
3. Push the Model to Hugging face Private Repository by changing your Acess Token in Notebook
4. Download the Quantized Model which is Pushed to Hugging face Repository which is in GGUF Format
5. Download the Ollama Software(Windows/Linux/MacOS)-https://ollama.com/download
6. Keep the downloaded Model and modelfile.txt in one Folder-(New Folder)
7. Run the Ollama Software on cmd to check whether Ollama has installed properly or not - 
## Code 
'''
C:\Users\Darshit>ollama 
'''
8. Edit the Model File.txt file and change the first line of the Model by the Model 
For Example
![Alt text](Example.png?raw=true "Screenshot of the ModelFile.txt")


9. In the aboave File change the name of the ModelFile in the starting with the downloaded Model File from HuggingFace from your Repo
10. Go to cmd again and run the following Ollama command to add the Model to Ollama
'
C:\Users\Darshit>ollama create <name of new_model> -f ModelFile.txt
'
11. Check whether the Model has added or not to the Ollama by running the following command
'
C:\Users\Darshit>ollama list
'
12. Run the Model and Minimize the Screen
13. Activate the Environment "Therapy" in the Command line by adding the command - "\Therapy\Scripts\activate"
14. Install the required dependencies in Visual Studio Code : `pip install -r requirements.txt`
15. Start the Streamlit app: `streamlit run app.py`

## Usage
1. Open the app in your browser by navigating to `http://localhost:8501`.
2. Enter a mental health topic or prompt in the input field.
3. Adjust the desired text length and output format.
4. Click the "Generate" button to generate text based on the provided topic.
5. View the generated text in the app's output section.

## Technologies Used
- Python
- Streamlit
- Transformers (Hugging Face)
- Unsloth

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## License
This project is licensed under the [Apache 2.0 License](LICENSE).

## Contact
For any inquiries or support, please contact [darshit.works@gmail.com].
